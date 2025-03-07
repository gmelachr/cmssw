#! /usr/bin/env cmsRun
# cmsRun trackingMaterialAnalyser fromDB=False

###################################################################
# Set default phase-2 settings
###################################################################
import Configuration.Geometry.defaultPhase2ConditionsEra_cff as _settings
_PH2_GLOBAL_TAG, _PH2_ERA = _settings.get_era_and_conditions(_settings.DEFAULT_VERSION)

import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing

process = cms.Process("MaterialAnalyser",_PH2_ERA)

options = VarParsing('analysis')

options.register('fromDB',
                 False,
                 VarParsing.multiplicity.singleton,
                 VarParsing.varType.bool,
                 'Read Geometry from DB?',
)

options.parseArguments()

if options.fromDB :
   process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
   from Configuration.AlCa.GlobalTag import GlobalTag
   process.GlobalTag = GlobalTag(process.GlobalTag, _PH2_GLOBAL_TAG, '')
else:
   process.load('Configuration.Geometry.GeometryExtendedRun4DefaultReco_cff')

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.files.LogTrackingMaterialAnalysis = dict()
process.MessageLogger.TrackingMaterialAnalysis=dict()

# Add our custom detector grouping to DDD
process.XMLIdealGeometryESSource.geomXMLFiles.extend(['SimTracker/TrackerMaterialAnalysis/data/trackingMaterialGroups_ForPhaseII.xml'])

# Analyze and plot the tracking material
process.load("SimTracker.TrackerMaterialAnalysis.trackingMaterialAnalyser_ForPhaseII_cff")
process.trackingMaterialAnalyser.SplitMode         = "NearestLayer"
process.trackingMaterialAnalyser.SaveParameters    = True
process.trackingMaterialAnalyser.SaveXML           = True
process.trackingMaterialAnalyser.SaveDetailedPlots = True

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring('file:material.root')
)

process.path = cms.Path(process.trackingMaterialAnalyser)


