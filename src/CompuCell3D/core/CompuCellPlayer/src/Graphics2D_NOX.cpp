#include "Graphics2D_NOX.h"


using namespace std;

Graphics2D_NOX::Graphics2D_NOX( const char *name): Graphics2DBase(name)
{

} 
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
Graphics2D_NOX::~Graphics2D_NOX(){

}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Graphics2D_NOX::produceImage(QImage & image){
   image=image2D;
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Graphics2D_NOX::preDrawTask(){
   image2D=QImage(labelSize,imageFormat);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Graphics2D_NOX::postDrawTask(){
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Graphics2D_NOX::initPainter(){
   painterPtr->begin(&image2D);
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void Graphics2D_NOX::paintBackground(const QColor & _color){
   painterPtr->setBrush(_color);
   painterPtr->fillRect(0,0,labelSize.width(),labelSize.height(),painterPtr->brush());
}

////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


