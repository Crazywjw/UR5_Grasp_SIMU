
"use strict";

let AddToLog = require('./AddToLog.js')
let RawRequest = require('./RawRequest.js')
let GetRobotMode = require('./GetRobotMode.js')
let GetLoadedProgram = require('./GetLoadedProgram.js')
let IsInRemoteControl = require('./IsInRemoteControl.js')
let IsProgramSaved = require('./IsProgramSaved.js')
let GetSafetyMode = require('./GetSafetyMode.js')
let GetProgramState = require('./GetProgramState.js')
let Popup = require('./Popup.js')
let IsProgramRunning = require('./IsProgramRunning.js')
let Load = require('./Load.js')

module.exports = {
  AddToLog: AddToLog,
  RawRequest: RawRequest,
  GetRobotMode: GetRobotMode,
  GetLoadedProgram: GetLoadedProgram,
  IsInRemoteControl: IsInRemoteControl,
  IsProgramSaved: IsProgramSaved,
  GetSafetyMode: GetSafetyMode,
  GetProgramState: GetProgramState,
  Popup: Popup,
  IsProgramRunning: IsProgramRunning,
  Load: Load,
};
