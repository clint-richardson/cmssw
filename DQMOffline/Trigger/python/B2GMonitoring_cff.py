import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.HLTEGTnPMonitor_cfi import egmGsfElectronIDsForDQM,egHLTDQMOfflineTnPSource

b2gDileptonHLTDQMOfflineTnPSource = egHLTDQMOFflineTnPSource.clone()
b2gDileptonHLTDQMOfflineTnPSource.tagAndProbeCollections = cms.VPSet(
         cms.PSet( 
            tagAndProbeConfigEle27WPTight,
            histConfigs = egammaStdHistConfigs,
            baseHistName = cms.string("eleWPTightTag_"),
            filterConfigs = cms.VPSet(
            cms.PSet(
                folderName = cms.string("HLT/EGTagAndProbeEffs/HLT_DoubleEle37_27_CaloIdL_GsfTrkIdVL"),
                rangeCuts = cms.VPSet(etRangeCut.clone(allowedRanges=cms.vstring("40:99999")),),
                filterName = cms.string("hltDiEle27CaloIdLGsfTrkIdVLDPhiUnseededFilter"),
                histTitle = cms.string(""),
                tagExtraFilter = cms.string(""),
                )
            ),
        ),
)

b2gMonitorHLT = cms.Sequence(
    egmGsfElectronIDsForDQM*
    b2gDileptonHLTDQMOfflineTnPSource
)
