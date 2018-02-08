        
#include "CellTypeMonitorPlugin.h"

#include <CompuCell3D/Simulator.h>
using namespace CompuCell3D;

#include <BasicUtils/BasicPluginProxy.h>

BasicPluginProxy<Plugin, CellTypeMonitorPlugin>
cellTypeMonitorProxy("CellTypeMonitor", "Autogenerated plugin - the author of the plugin should provide brief description here",
         &Simulator::pluginManager);
