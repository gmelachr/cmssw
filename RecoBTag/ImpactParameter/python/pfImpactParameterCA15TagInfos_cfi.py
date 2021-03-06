import FWCore.ParameterSet.Config as cms

from RecoBTag.ImpactParameter.pfImpactParameterTagInfos_cfi import *

pfImpactParameterCA15TagInfos = pfImpactParameterTagInfos.clone(
    computeProbabilities = cms.bool(False),
    computeGhostTrack = cms.bool(False),
    jets = cms.InputTag("ca15PFJetsCHS"),
    maxDeltaR = cms.double(1.5)
)
