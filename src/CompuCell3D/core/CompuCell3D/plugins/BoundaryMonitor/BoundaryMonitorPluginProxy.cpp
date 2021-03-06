        
#include "BoundaryMonitorPlugin.h"

#include <CompuCell3D/Simulator.h>
using namespace CompuCell3D;

#include <BasicUtils/BasicPluginProxy.h>

BasicPluginProxy<Plugin, BoundaryMonitorPlugin>
boundaryMonitorProxy("BoundaryMonitor", "Autogenerated plugin - the author of the plugin should provide brief description here",
         &Simulator::pluginManager);
