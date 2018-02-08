//
// TextConverter.cpp
//
// $Id: //poco/1.4/Foundation/src/TextConverter.cpp#1 $
//
// Library: Foundation
// Package: Text
// Module:  TextConverter
//
// Copyright (c) 2004-2006, Applied Informatics Software Engineering GmbH.
// and Contributors.
//
// Permission is hereby granted, free of charge, to any person or organization
// obtaining a copy of the software and accompanying documentation covered by
// this license (the "Software") to use, reproduce, display, distribute,
// execute, and transmit the Software, and to prepare derivative works of the
// Software, and to permit third-parties to whom the Software is furnished to
// do so, all subject to the following:
// 
// The copyright notices in the Software and this entire statement, including
// the above license grant, this restriction and the following disclaimer,
// must be included in all copies of the Software, in whole or in part, and
// all derivative works of the Software, unless such copies or derivative
// works are solely in the form of machine-executable object code generated by
// a source language processor.
// 
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
// IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
// FITNESS FOR A PARTICULAR PURPOSE, TITLE AND NON-INFRINGEMENT. IN NO EVENT
// SHALL THE COPYRIGHT HOLDERS OR ANYONE DISTRIBUTING THE SOFTWARE BE LIABLE
// FOR ANY DAMAGES OR OTHER LIABILITY, WHETHER IN CONTRACT, TORT OR OTHERWISE,
// ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
// DEALINGS IN THE SOFTWARE.
//


#include "Poco/TextConverter.h"
#include "Poco/TextIterator.h"
#include "Poco/TextEncoding.h"


namespace {
	int nullTransform(int ch)
	{
		return ch;
	}
}


namespace Poco {


TextConverter::TextConverter(const TextEncoding& inEncoding, const TextEncoding& outEncoding, int defaultChar):
	_inEncoding(inEncoding),
	_outEncoding(outEncoding),
	_defaultChar(defaultChar)
{
}


TextConverter::~TextConverter()
{
}


int TextConverter::convert(const std::string& source, std::string& destination, Transform trans)
{
	int errors = 0;
	TextIterator it(source, _inEncoding);
	TextIterator end(source);
	unsigned char buffer[TextEncoding::MAX_SEQUENCE_LENGTH];

	while (it != end)
	{
		int c = *it;
		if (c == -1) { ++errors; c = _defaultChar; }
		c = trans(c);
		int n = _outEncoding.convert(c, buffer, sizeof(buffer));
		if (n == 0) n = _outEncoding.convert(_defaultChar, buffer, sizeof(buffer));
		poco_assert (n <= sizeof(buffer));
		destination.append((const char*) buffer, n);
		++it;
	}
	return errors;
}


int TextConverter::convert(const void* source, int length, std::string& destination, Transform trans)
{
	poco_check_ptr (source);

	int errors = 0;
	const unsigned char* it  = (const unsigned char*) source;
	const unsigned char* end = (const unsigned char*) source + length;
	unsigned char buffer[TextEncoding::MAX_SEQUENCE_LENGTH];
	
	while (it < end)
	{
		int n = _inEncoding.queryConvert(it, 1);
		int uc;
		int read = 1;

		while (-1 > n && (end - it) >= -n)
		{
			read = -n;
			n = _inEncoding.queryConvert(it, read);
		}

		if (-1 > n)
		{
			it = end;
		}
		else
		{
			it += read;
		}

		if (-1 >= n)
		{
			uc = _defaultChar;
			++errors;
		}
		else
		{
			uc = n;
		}

		uc = trans(uc);
		n = _outEncoding.convert(uc, buffer, sizeof(buffer));
		if (n == 0) n = _outEncoding.convert(_defaultChar, buffer, sizeof(buffer));
		poco_assert (n <= sizeof(buffer));
		destination.append((const char*) buffer, n);
	}
	return errors;
}


int TextConverter::convert(const std::string& source, std::string& destination)
{
	return convert(source, destination, nullTransform);
}


int TextConverter::convert(const void* source, int length, std::string& destination)
{
	return convert(source, length, destination, nullTransform);
}


} // namespace Poco
