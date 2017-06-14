import FWCore.ParameterSet.Config as cms

from DQMOffline.Trigger.HLTEGTnPMonitor_cfi import egmGsfElectronIDsForDQM,egHLTDQMOfflineTnPSource
from DQMOffline.Trigger.topDiLeptonHLTEventDQM_cfi import topDiLeptonHLTOfflineDQM

b2gDielectronHLTDQMOfflineTnPSource = egHLTDQMOFflineTnPSource.clone()
b2gDielectronHLTDQMOfflineTnPSource.tagAndProbeCollections = cms.VPSet(
         cms.PSet( 
            tagAndProbeConfigEle27WPTight,
            histConfigs = egammaStdHistConfigs,
            baseHistName = cms.string("eleWPTightTag_"),
            filterConfigs = cms.VPSet(
            cms.PSet(
                folderName = cms.string("HLT/B2GHLTOffline/Dileptonic/HLT_DoubleEle37_27_CaloIdL_GsfTrkIdVL"),
                rangeCuts = cms.VPSet(etRangeCut.clone(allowedRanges=cms.vstring("40:99999")),),
                filterName = cms.string("hltDiEle27CaloIdLGsfTrkIdVLDPhiUnseededFilter"),
                histTitle = cms.string(""),
                tagExtraFilter = cms.string(""),
                )
            ),
        ),
)

b2gDileptonHLTOfflineDQM = topDiLeptonHLTOfflineDQM.clone()
b2gDileptonHLTOfflineDQM.setup.directory = cms.string('HLT/B2GHLTOffline/Dileptonic/CrossTriggers')
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsELECMU = cms.vstring(['HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL_v','HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL_v'])
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsDIMUON = cms.vstring([''])
b2gDileptonHLTOfflineDQM.setup.triggerExtras.pathsDIELEC = cms.vstring([''])
b2gDileptonHLTOfflineDQM.preselection.trigger.select = cms.vstring(['HLT_Mu37_Ele27_CaloIdL_GsfTrkIdVL_v','HLT_Mu27_Ele37_CaloIdL_GsfTrkIdVL_v'])

b2gDimuonHLTOfflineDQM = topDiLeptonHLTOfflineDQM.clone()
b2gDimuonHLTOfflineDQM.setup.directory = cms.string('HLT/B2GHLTOffline/Dileptonic/Dimuon')
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsELECMU = cms.vstring([''])
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsDIMUON = cms.vstring(['HLT_Mu30_TkMu11_v'])
b2gDimuonHLTOfflineDQM.setup.triggerExtras.pathsDIELEC = cms.vstring([''])
b2gDimuonHLTOfflineDQM.preselection.trigger.select = cms.vstring(['HLT_Mu30_TkMu11'])



b2gMonitorHLT = cms.Sequence(
    egmGsfElectronIDsForDQM*
    b2gDielectronHLTDQMOfflineTnPSource*
    b2gDileptonHLTOfflineDQM*
    b2gDimuonHLTOfflineDQM

)
