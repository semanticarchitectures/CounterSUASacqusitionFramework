**AIR FORCE**  
**COUNTER-UNMANNED SYSTEMS**  
**DOCTRINE AND POLICY**

*Command and Control Systems Engineering Reference*

January 2026

**UNCLASSIFIED**

# **EXECUTIVE SUMMARY**

**Purpose.** This document provides Air Force doctrine and policy guidance for Counter-Unmanned Systems (C-US) operations, with specific emphasis on Command and Control (C2) systems engineering requirements. It synthesizes current operational doctrine, recent policy directives, and strategic imperatives to inform the development of integrated C-US C2 capabilities.

**Scope.** This document addresses C-US operations across all domains with particular focus on airspace below the Coordinating Altitude, where the proliferation of small Unmanned Aircraft Systems (sUAS) and loitering munitions presents unique challenges to airspace control and integrated air defense.

**Key Findings.** Current Air Force doctrine provides the foundational framework for C-US operations, but implementation requires significant technological development.

* Saturation of airspace below Coordinating Altitude with diverse unmanned systems  
* Integration challenges across Theater Air-Ground System (TAGS) elements  
* Deconfliction requirements for manned aircraft, UAS, loitering munitions, and fires  
* Scalability demands driven by adversary drone dominance strategies

# **1\. DOCTRINAL FOUNDATIONS**

## **1.1 Core Airpower Principles**

Air Force Doctrine Publication (AFDP) 1 establishes that "control of the air is a precondition for control of the surface." This foundational principle remains valid in the era of unmanned systems proliferation. C-US operations must be understood as an integral component of counterair operations across the full spectrum of conflict.

## **1.2 Joint Doctrine Integration**

Joint Publication (JP) 3-52, Joint Airspace Control, and JP 3-01, Countering Air and Missile Threats, provide the doctrinal framework for C-US integration into joint operations. Key principles include:

* Airspace Control Authority (ACA): The Joint Force Commander designates the ACA with overall responsibility for airspace control within the Joint Operations Area.  
* Airspace Control Methods: Both positive control (continuous electronic monitoring) and procedural control (pre-agreed procedures) apply to UAS operations.  
* Theater Air-Ground System (TAGS): C-US capabilities must integrate across TAGS components including TACS, AAGS, NTACS, and MACCS.

# **2\. AIRSPACE CONTROL ARCHITECTURE**

## **2.1 Coordinating Altitude and Delegation**

The Coordinating Altitude (CA) serves as an Airspace Coordinating Measure (ACM) that procedurally separates users and defines transitions between airspace control elements. The CA allows the ACA to assign a volume of airspace to another control organization, typically delegating airspace below the CA to the land component commander.

## **2.2 Coordination Measures**

Multiple coordination measures apply to C-US operations:

* Coordinating Altitude (CA): Separates airspace control responsibilities  
* Coordination Level (CL): Designates level below which fixed-wing aircraft normally will not fly  
* Minimum Risk Route (MRR): Designated route to minimize exposure to friendly air defense  
* Restricted Operations Zone (ROZ): Airspace to segregate certain flight activities  
* Base Defense Zone (BDZ): Airspace volume around military installation for organic C-UAS

# **3\. COMMAND AND CONTROL REQUIREMENTS**

## **3.1 Detection and Tracking**

The fundamental C-US challenge is achieving reliable detection, tracking, and identification of UAS in complex environments. C2 systems must integrate diverse sensor inputs:

* Radio Frequency (RF): Detection of command links and telemetry  
* Radar: Specialized low-altitude, slow-moving target radars with clutter rejection  
* Electro-Optical/Infrared (EO/IR): Visual and thermal detection with positive identification  
* Acoustic: Detection of motor/rotor noise in localized areas  
* Networked Sensors: Distributed sensor networks with track fusion

## **3.2 Identification and Classification**

C2 systems must support rapid friend-or-foe determination through cooperative identification (IFF/SIF transponders, ADS-B), non-cooperative identification (geolocation correlation, signature libraries, behavioral analysis), and intelligence integration (threat libraries, forensics data).

## **3.3 Decision Support and Engagement Coordination**

C2 systems must provide decision support tools enabling rapid engagement decisions under time-compressed scenarios including threat prioritization, weapon-target pairing, deconfliction automation, multi-domain coordination, and rules of engagement enforcement.

# **4\. INTEGRATED AIR AND MISSILE DEFENSE**

## **4.1 C-UAS Within IAMD Architecture**

C-UAS operations are a component of IAMD, not a separate stovepipe. AFDP 3-01 establishes that Air and Missile Defense includes actions to counter enemy manned aircraft, UAS, aerodynamic missiles, and ballistic missiles. IAMD functions applied to C-US include passive defense (hardening, concealment, deception), active defense (kinetic and non-kinetic effects), and offensive counterair (attack operations against launch sites and C2 nodes).

## **4.2 C-UAS Effectors**

C2 systems must integrate diverse kinetic and non-kinetic effectors:

* Kinetic Guns: Low cost-per-shot, short range, effective against Group 1-2 UAS  
* Kinetic Missiles: Extended range, high precision (Stinger, AIM-9X)  
* Directed Energy: High-energy lasers, high-power microwave, near-zero cost-per-shot  
* Electronic Attack: RF jamming, GPS denial, cyber exploitation  
* Counter-UAS Nets: Physical capture for forensics/exploitation

# **5\. HOMELAND DEFENSE CONSIDERATIONS**

## **5.1 Authority and Responsibility**

JP 3-27, Joint Homeland Defense, and AFDP 3-27, Homeland Operations, establish a fundamentally different operational framework for homeland C-UAS:

* NORAD Authority: DoD maintains sole responsibility for defending against air threats in U.S. airspace  
* FAA Airspace Control: FAA typically retains role as Airspace Control Authority in the National Airspace System  
* Interagency Coordination: DoD relies on FAA and DHS for detection and identification  
* Title 10 U.S.C. § 130i: Provides DoD authority with significant restrictions on use of force

## **5.2 Policy Framework Evolution**

Executive Order 14305, "Restoring American Airspace Sovereignty" (June 6, 2025), signals significant policy evolution regarding homeland C-UAS authorities, emphasizing enhanced detection, streamlined coordination, expanded DoD capabilities, and clarification of engagement authorities.

# **6\. SYSTEMS ENGINEERING IMPLICATIONS**

## **6.1 Architecture Requirements**

C-UAS C2 systems must be architected for integration, not isolation:

* Open Architecture: Modular, standards-based interfaces enabling rapid integration  
* Scalability: Architecture must scale from single-installation to theater-wide defense  
* Resilience: Distributed processing, mesh networking, graceful degradation  
* Interoperability: Native integration with TAGS elements and joint C2 systems  
* AI/ML Integration: Leverage artificial intelligence for classification and decision support

## **6.2 Data Standards and Interfaces**

Critical data exchange standards for C-UAS C2 systems include NATO STANAG 4607 (GMTI), STANAG 4676 (ISR), Link 16 J-series messages, VMF (Variable Message Format), STANAG 4609 (Video), MISB standards for metadata, and NATO Air C2 Information Services (ACIS).

## **6.3 Performance Requirements**

Operationally-derived performance requirements include:

* Track Update Rate: 1-2 Hz for UAS tracks  
* Track Capacity: 1,000+ simultaneous tracks  
* Detection-to-Engagement: \< 30 seconds  
* Common Operating Picture Latency: \< 2 seconds end-to-end  
* Availability: 99.9% uptime  
* Cyber Resilience: Impact Level 5 (IL5) or higher

# **7\. POLICY AND GOVERNANCE**

## **7.1 Joint Interagency Task Force 401**

The August 27, 2025, Secretary of Defense memorandum establishing Joint Interagency Task Force 401 (JIATF 401\) represents a fundamental reorganization of DoD C-UAS governance. Key provisions:

* Consolidated Authority: JIATF 401 Director has acquisition and procurement authority  
* Service Integration: Services designate personnel with C-UAS competencies  
* Approval Authority: JIATF 401 Director determines whether new Service-specific C-UAS systems will be adopted  
* Dedicated Test Range: USD(R\&E) directed to establish dedicated C-UAS test and training range  
* Multi-year Funding: Pursuit of flexible RDT\&E, procurement, and O\&M funding

## **7.2 DoD Strategy for Countering Unmanned Systems**

The December 1, 2024, DoD Strategy articulates five strategic ways:

1. Deepen Understanding and Awareness: C2 systems incorporate threat intelligence and forensics  
2. Disrupt & Degrade Threat Networks: C2 systems provide targeting data for offensive operations  
3. Defend Against Threats: Integration of active and passive defenses  
4. Deliver Solutions with Speed, Adaptability, and Scale: Rapid acquisition and modular solutions  
5. Develop & Design Future Joint Force: C-UAS as key element of force development

# **8\. IMPLEMENTATION GUIDANCE**

## **8.1 Near-Term Actions (0-18 months)**

* Standardize C-UAS track formats: Develop Link 16 extensions and VMF schemas  
* Integrate C-UAS into ACO/SPINS: Develop digital ACO extensions  
* Establish C2 system interoperability testing: Leverage Joint Interoperability Test Command  
* Pilot AI-assisted decision support: Deploy ML models for target classification  
* Update Rules of Engagement templates: Develop ROE annexes for UAS engagement

## **8.2 Mid-Term Actions (18-36 months)**

* Deploy integrated C-UAS C2 capability: Field systems integrating detection and engagement  
* Operationalize counter-swarm capabilities: Deploy C2 with automated multi-target tracking  
* Expand coalition interoperability: Demonstrate C-UAS C2 with NATO and allies  
* Establish C-UAS training pipeline: Expand Joint C-sUAS University curriculum  
* Develop mission command applications: Field mobile C-UAS C2 capabilities

## **8.3 Long-Term Actions (36+ months)**

* Full JADC2 integration: Integrate C-UAS as native element of Joint All-Domain C2  
* Autonomous engagement capabilities: Deploy AI-enabled autonomous engagement systems  
* Predictive threat analysis: Leverage big data analytics and predictive modeling  
* Quantum-resistant cybersecurity: Implement post-quantum cryptographic algorithms  
* Space-based C-UAS integration: Integrate overhead persistent infrared and SAR

# **REFERENCES**

## **Joint and Department of Defense Publications**

* DoD Strategy for Countering Unmanned Systems, December 1, 2024  
* DoD Directive 3800.01E, "DoD Executive Agent for Counter Small Unmanned Aircraft Systems," February 21, 2020  
* JP 3-01, Countering Air and Missile Threats, 21 April 2023  
* JP 3-10, Joint Security Operations in Theater, 25 November 2019  
* JP 3-27, Joint Homeland Defense, 10 July 2018  
* JP 3-30, Joint Air Operations, 25 July 2019  
* JP 3-52, Joint Airspace Control, 13 November 2014 (Change 1, 27 May 2022\)

## **Air Force Publications**

* Air Force Doctrine Advisory, Control Below the Coordinating Altitude, 21 August 2025  
* AFDP 1, The Air Force, 21 August 2023  
* AFDP 3-01, Counterair Operations, 20 May 2022  
* AFDP 3-27, Homeland Operations, 5 July 2021  
* AFDP 3-52, Airspace Control, 31 December 2021

## **Policy Documents**

* Executive Order 14305, "Restoring American Airspace Sovereignty," June 6, 2025  
* Secretary of Defense Memorandum, "Establishment of Joint Interagency Task Force 401," August 27, 2025  
* Title 10, United States Code, Section 130i, "Protection of certain facilities and assets from unmanned aircraft"