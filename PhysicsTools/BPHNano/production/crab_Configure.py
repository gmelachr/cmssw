from CRABClient.UserUtilities import config, ClientException#, getUsernameFromCRIC
#from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Data_2023_C1_7'#'BuToJpsiKplus_2022_biased'
config.General.workArea = 'Data_2023_C1_7'#BuToJpsiKplus_2022_biased_cmssw_12' 
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../test/run_bphNano_cfg.py'
config.JobType.maxMemoryMB = 4000
config.JobType.maxJobRuntimeMin = 3000
config.JobType.allowUndistributedCMSSW = True

config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions23/Cert_Collisions2023_366442_370790_Golden.json'
#config.Data.lumiMask = 'https://cms-service-dqmdc.web.cern.ch/CAF/certification/Collisions22/Cert_Collisions2022_355100_362760_Golden.json'
config.Data.allowNonValidInputDataset = True
#config.Data.userInputFiles = open('BdToJpsiKshort_SSDCP_biased_miniAOD.txt').readlines()
config.Data.inputDataset = '/ParkingDoubleMuonLowMass7/Run2023C-PromptReco-v1/MINIAOD'#'/ButoJpsiK_Jpsito2Mu_MuFilter_TuneCP5_13p6TeV_pythia8-evtgen/Run3Summer22MiniAODv3-124X_mcRun3_2022_realistic_v12-v2/MINIAODSIM'#'/ButoJpsiK_Jpsito2Mu_MuFilter_TuneCP5_13p6TeV_pythia8-evtgen/Run3Summer22MiniAODv4-130X_mcRun3_2022_realistic_v5-v2/MINIAODSIM'#'/ButoJpsiK_Jpsito2Mu_MuFilter_TuneCP5_13p6TeV_pythia8-evtgen/Run3Summer23MiniAODv4-130X_mcRun3_2023_realistic_v14-v3/MINIAODSIM'
#config.Data.outputPrimaryDataset = 'BuToJpsiKplus_2022_biased'
config.Data.splitting = 'LumiBased'
config.Data.unitsPerJob = 20
#config.Data.totalUnits = 487
config.Data.outLFNDirBase = '/store/group/cmst3/group/bpark/gmelachr/Data_TEST/2022'#cmssw_15_1_0_pre1_deactivate_fixtrack'
config.Data.publication = False
config.Data.outputDatasetTag = config.General.requestName
config.Data.ignoreLocality = True

config.Site.whitelist = []
config.Site.storageSite = 'T2_CH_CERN'

