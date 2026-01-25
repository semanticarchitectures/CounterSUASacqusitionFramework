// SysML v2 model: Counter-SUAS System with Protected Regions
package counter_suas {

  // === Definitions ===
  part def ProtectedRegion {
    attribute name: String;
    attribute geometry: String; // polygon, volume, corridor, moving
    attribute altitudeFloor: Real;
    attribute altitudeCeiling: Real;
    attribute farThreshold: Real; // false alarm rate threshold
  }

  part def ThreatTarget {
    attribute id: String;
    attribute trajectoryType: String; // predetermined | dynamic | stochastic
    attribute speed: Real;
    attribute altitude: Real;
    attribute intent: String; // benign | unknown | hostile
  }

  part def DataFeed {
    attribute feedType: String; // ADSB, weather, RF, external tracks
  }

  part def Sensor {
    attribute sensorType: String; // radar, RF, EOIR, acoustic
    attribute location: String;
    attribute maxRange: Real;
  }

  part def DecisionSupport {
    attribute classificationConfidenceMin: Real;
    attribute responseTimeMax: Real;
  }

  part def CommandControl {
    attribute roeMode: String; // human_in_loop | auto
  }

  part def Effector {
    attribute effectorType: String; // EW, kinetic, DE
    attribute authorizationRequired: Boolean;
  }

  // === Behavior / Constraints ===
  constraint def DetectionProbability {
    in sensorType: String;
    in range: Real;
    in orientation: Real;
    in relativeVelocity: Real;
    in clutter: Real;
    out pd: Real;
  }

  // === System Definition ===
  part def CounterSuasSystem {
    part regions: ProtectedRegion[*];
    part feeds: DataFeed[*];
    part sensors: Sensor[*];
    part decisionSupport: DecisionSupport[1];
    part commandControl: CommandControl[1];
    part effectors: Effector[*];

    // Interfaces
    port inTelemetry;
    port outAlerts;
    port outMitigationTasks;
  }

  // === Requirement Stubs ===
  requirement def ReqDetectionPd {
    attribute id = "REQ-DET-001";
    attribute text = "Pd shall be >= threshold as a function of range and sensor type.";
  }

  requirement def ReqFalseAlarmRate {
    attribute id = "REQ-RISK-001";
    attribute text = "FAR shall not exceed region-specific threshold.";
  }

  requirement def ReqResponseTime {
    attribute id = "REQ-C2-001";
    attribute text = "Response time from detection to action shall be <= max.";
  }
}

