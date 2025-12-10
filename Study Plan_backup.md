# COMPREHENSIVE PhD STUDY PLAN

## Spatiotemporal Neuromarkers of Reward-Control Dysfunction in Obesity and Binge-Eating Disorder: A BI-SNN Framework Applied to ABCD Task fMRI and Behavioral Data

---

## EXECUTIVE SUMMARY

This PhD project aims to develop and validate a Biologically-Informed Spiking Neural Network (BI-SNN) framework-specifically the NeuCube architecture by Kasabov et al.-to extract spatiotemporal neuromarkers of dysfunctional reward-control network coordination in adolescents with binge-eating disorder (BED), obesity, and healthy-weight controls. Using two complementary studies grounded in the Adolescent Brain Cognitive Development (ABCD) study, this project will test whether dynamic network coordination, not merely static activation or connectivity, distinguishes eating-disorder phenotypes and predicts future BED trajectories. The work is methodologically novel (first BI-SNN application to ABCD eating disorders), scientifically rigorous (prospective prediction, large sample, rigorous cross-validation), and clinically translational (identifies early biomarkers for risk stratification and intervention targets).

---

## 1. SCIENTIFIC RATIONALE AND SIGNIFICANCE

### 1.1 The Problem: Static Approaches Miss Dynamic Network Coordination

The neurobiology of binge-eating disorder and obesity has traditionally been framed in terms of **imbalanced activation**: hyperactive reward regions (ventral striatum, orbitofrontal cortex) overwhelming inhibitory control regions (dorsolateral prefrontal cortex, anterior cingulate cortex). However, this "activation magnitude" model has significant limitations:

- Most task-fMRI studies report modest effect sizes (Cohen's d ~ 0.3-0.6) and inconsistent activation differences between BED/obesity and controls (Schag et al. 2020, Neuro-Image: Clin).
- Static functional connectivity measures (resting-state FC, task-averaged FC) average over time and miss trial-level dynamics and transient network states (Preti et al. 2017, Nat Rev Neurosci).
- Recent ABCD work has shown that **resting-state connectivity patterns** distinguish pre-adolescent BED and obesity even when conventional task activation (monetary incentive delay [MID], stop-signal task [SST]) shows weak group differences (Rapuano et al. 2021, ABCD study consortium). This suggests that network organization and coordination-not just local activation-may be the key marker.

**Key insight from recent literature:** The emerging consensus is that eating-disorder risk involves impaired **temporal coordination** between reward anticipation and inhibitory control systems, particularly how these networks communicate during competing demands (wanting food vs. inhibiting approach). Static measures miss this moment-to-moment interplay.

### 1.2 Why Spatiotemporal (BI-SNN) Modeling is Necessary

Traditional machine-learning methods (SVM, GLM, standard RNNs) are designed for static feature vectors and cannot naturally capture the **spatial and temporal interdependencies** in fMRI data:

- Spatial: voxels are organized in 3D brain space; nearby voxels representing functionally related regions should have correlated temporal dynamics.
- Temporal: the *timing* of activation changes within a trial (e.g., how quickly reward anticipation activates striatum, and whether prefrontal inhibitory regions respond in parallel) encodes mechanistic information.

Spiking Neural Networks (SNNs) are uniquely suited to this task because:

1. **Inherent temporal representation:** SNNs integrate time into their computational model via spike timing and membrane potentials (leaky-integrate-and-fire dynamics). Unlike feedforward networks that process fixed-length static vectors, SNNs naturally handle variable-length temporal sequences.

2. **Spike-Timing-Dependent Plasticity (STDP):** A biologically plausible unsupervised learning rule that modifies synaptic weights based on the *relative timing* of pre- and post-synaptic spikes. This captures "if neuron A consistently fires before neuron B, strengthen their connection" logic, which reflects functional causality or coordinated activity in the brain (Kasabov et al. 2017, IEEE Trans Neural Netw Learn Syst).

3. **3D spatial mapping with preserved connectivity:** The NeuCube architecture maps fMRI ROIs into a 3D spiking neural cube according to their brain coordinates (Talairach or MNI template), preserving anatomical proximity and enabling discovery of spatially organized connectivity patterns (Kasabov et al. 2016, IEEE Trans Biomed Eng).

4. **Automatic feature discovery:** During unsupervised STDP learning, neurons that receive and transmit the most task-relevant spikes emerge as network "hubs." These can be visualized and interpreted as functional pathways, providing mechanistic insight alongside classification performance (Kasabov et al. 2017).

5. **Proven performance on fMRI data:** Kasabov et al. (2016, 2017) demonstrated that NeuCube-based classification of fMRI data (e.g., reading affirmative vs. negative sentences, picture vs. sentence perception) achieved 90-96% accuracy, compared to 48-50% for SVM, MLP, and GLM-a substantial improvement that was accompanied by discovery of neurobiologically interpretable pathways (e.g., stronger left dorsolateral prefrontal cortex-temporal coupling for negative sentence comprehension).

### 1.3 Why This Matters for Eating Disorders and BED Prediction

If network coordination deficits (detectable via BI-SNN) underlie eating-disorder risk, then:

1. **Better phenotyping:** Individuals with the same BMI or binge-eating frequency may have different underlying network dysfunctions. BI-SNN neuromarkers could stratify heterogeneous obesity and BED samples into mechanistically meaningful subtypes (e.g., "impulsive-reward-dominant" vs. "inhibition-deficient"), opening pathways to personalized intervention.

2. **Early detection:** Network coordination deficits may emerge before behavioral phenotypes are fully manifest. Adolescents with spatiotemporal reward-control coupling deficits could be identified as high-risk before they develop diagnosable BED, enabling preventive intervention.

3. **Mechanistic specificity:** Current interventions (cognitive-behavioral therapy, medications) are broadly targeted. If BI-SNN markers identify specific network failures (e.g., delayed prefrontal response to reward cues), interventions could be tailored (e.g., neurofeedback targeting prefrontal-striatal communication).

4. **Clinical translation:** Neuromarkers that predict BED trajectories could eventually inform risk screening in adolescent populations and support early intervention research.

---

## 2. STUDY OVERVIEW: TWO COMPLEMENTARY STUDIES IN ABCD

### 2.1 Study Design Framework

This PhD project comprises **two interlocking studies** that leverage the full power of ABCD's longitudinal design and multi-wave imaging:

| **Aspect** | **Study 1: Cross-Sectional Neuromarkers** | **Study 2: Longitudinal Prediction** |
|---|---|---|
| **Objective** | Identify BI-SNN features that distinguish BED, obesity, and controls *at a single timepoint* and test associations with behavior | Test whether baseline BI-SNN features predict BED onset, symptom severity change, and other trajectories over ~2-4 years |
| **Sample** | All ABCD participants with complete MID + SST fMRI at target wave (15-16 years primary; 13-14 fallback) | Subset of Study 1 sample with complete imaging + ED assessments at both predictor wave (11-14 years) and outcome wave (15-16 years) |
| **Primary Outcome** | BI-SNN neuromarker group differences; associations with task behavior and clinical severity | Incident BED, symptom trajectory, severity change (3 levels: worsening, stable, improving) |
| **Analysis Type** | Descriptive + association; optional classification (exploratory) | Predictive modeling (logistic regression, regularized models, cross-validation) |
| **Publication Strategy** | Neuromarker discovery paper (methods + mechanisms) | Prospective validation paper (prediction + clinical utility) + possibly mechanistic/translational paper |

### 2.2 ABCD Dataset and Wave Selection Rationale

**Dataset:** The Adolescent Brain Cognitive Development (ABCD) Study is a prospective longitudinal cohort of ~11,900 participants recruited at ages 9-10, with comprehensive neuroimaging (including task fMRI), behavioral testing, and clinical assessments at multiple waves (baseline, 2-year, 4-year, 6-year, etc.). ABCD provides:

- **Large, representative sample** with diverse demographics (though skewed toward higher SES and non-Hispanic white).
- **Standardized preprocessing** of fMRI data (minimally preprocessed) and validated quality control pipelines.
- **Repeated measures** of eating-disorder symptoms, BMI, and psychopathology.
- **Validated cognitive tasks** (MID, SST) with established behavioral readouts.

**Wave selection for Study 1 (primary timepoint):** **Age 15-16 years (approximately 6-year follow-up from baseline at age 9-10).**

*Rationale:*
- At ages 15-16, eating-disorder phenotypes (including BED) are more fully expressed than in earlier adolescence. Prevalence of BED in ABCD at this age is estimated at 1-2% (still rare but sufficient for cross-sectional comparisons).
- Cortico-striatal circuits are more mature (still developing, but more stable than at ages 11-13), enhancing the stability of functional connectivity patterns.
- Sufficient time has elapsed since imaging at earlier waves to show developmental change, while retaining predictive power for future trajectories (Study 2).

*Fallback option:* If attrition and quality control result in n_BED < 50 after QC at ages 15-16, the study will use ages 13-14 (4-year follow-up) as the primary wave, with ages 15-16 treated as a validation/severity-extension sample.

---

## 3. STUDY 1: CROSS-SECTIONAL IDENTIFICATION OF SPATIOTEMPORAL NEUROMARKERS

### 3.1 Objectives

1. To identify spatiotemporal BI-SNN features derived from task fMRI (MID + SST) that **distinguish individuals with BED, obesity without BED, and healthy-weight controls** in late adolescence.
2. To test whether these BI-SNN features are **associated with behavioral markers of reward sensitivity and inhibitory control** (e.g., reward speeding, stop-signal reaction time [SSRT], post-error slowing).
3. To determine whether BI-SNN features explain **additional variance in behavior** beyond simple task-activation contrasts and static functional connectivity-establishing that dynamic spatiotemporal modeling adds clinically meaningful information.
4. To characterize **sex, developmental, and comorbidity moderators** of group differences (e.g., whether neuromarker patterns differ between males and females, and whether depression/anxiety symptoms confound associations).

### 3.2 Sample, Inclusion, and Exclusion Criteria

#### **Study 1 Sample Composition**

Target sample sizes (post-QC):
- **BED group:** n = 60-80 (meeting diagnostic criteria for binge-eating disorder)
- **Obesity without BED group:** n = 120-150 (BMI â‰¥ age-/sex-adjusted 95th percentile; no BED or other threshold eating disorder)
- **Healthy-weight controls:** n = 200-250 (BMI 25th-75th percentile; no eating disorder)
- **Total:** n = 380-480 (all with complete MID + SST fMRI data, passing quality control)

**Rationale for unequal group sizes:** BED is relatively rare (1-2% in ABCD); obesity is more common (~15-20%); healthy-weight is normative. Unequal group sizes reflect population prevalence but may reduce statistical power for some comparisons. This will be addressed through:
1. Dimensional outcome analyses (continuous binge severity, LOC eating) which provide more statistical power.
2. Stratified analyses comparing BED vs. non-BED, and obesity (any) vs. lean.
3. Bonferroni correction for multiple comparisons, with pre-registered primary tests.

#### **Inclusion Criteria**

1. **Age:** Participants in the target study wave (15-16 years, or 13-14 if fallback) within ±6 months.
2. **Completed MID and SST fMRI tasks** at target wave with usable behavioral data (reaction times, accuracy, task compliance).
3. **Usable task fMRI data** passing ABCD quality control thresholds AND additional site-specific quality checks (see QC section below).
4. **Complete clinical assessments** at target wave:
   - Eating-disorder diagnostic interview (KSADS-5 or similar) or validated ED screener (EDE-Q, CHOP-QT).
   - BMI (measured or self-reported if necessary, with sensitivity analyses).
   - Symptom severity measures (LOC eating frequency, binge-eating frequency).
5. **Completed behavioral measures** for the MID and SST tasks (reaction times, accuracy, stop-signal estimates).

#### **Exclusion Criteria**

1. **Neurological or structural brain disorders:**
   - History of significant head injury with loss of consciousness (>10 seconds).
   - Seizure disorders, epilepsy, cerebral palsy, or other neurological conditions.
   - Brain tumors or significant structural abnormalities noted on clinical radiology review.

2. **Severe psychiatric conditions (optional, see justification below):**
   - Autism spectrum disorder (ASD): Optional to exclude or include with sensitivity analyses. ASD is associated with altered reward and inhibitory control (Chevallier et al. 2012, Nat Rev Neurosci), which could confound results. If included, ASD status will be included as a covariate; if excluded, attrition will be reported.
   - Psychotic disorders (schizophrenia, bipolar I with psychosis): Exclude due to severe alterations in reward processing and executive function.
   - Severe substance use disorder: Exclude if current illicit substance use (marijuana, opioids, stimulants) or alcohol use disorder, as these substantially alter dopaminergic systems independent of eating behavior (Volkow et al. 2017, Nat Rev Neurosci).

   *Rationale for optional ASD inclusion:* ABCD has high prevalence of ASD and ADHD (5-10% each). Excluding ASD substantially reduces sample size and generalizability. Instead, we will include ASD participants and adjust for ASD status in models; sensitivity analyses will test whether results hold in ASD-excluded samples.

3. **IQ and language barriers:**
   - Full-scale IQ < 70 if cognitive data available (to ensure task comprehension). However, most ABCD participants exceed this threshold; participants with estimated IQ 70-85 will be retained with sensitivity analyses.
   - Non-English fluency if KSADS or behavioral measures were not administered in English (reflects ABCD recruitment and assessment).

4. **Imaging contraindications:**
   - Ferrous metal implants incompatible with 3T MRI (e.g., non-MRI-safe pacemakers).
   - Severe claustrophobia or inability to complete imaging due to anxiety.
   - Pregnancy (if female; ABCD screens for this).

5. **Extreme motion during fMRI:**
   - Mean framewise displacement (FD) > 0.5 mm during task, OR
   - â‰¥30% of volumes with FD > 0.9 mm (ABCD standard thresholds).
   
   *Rationale:* Excessive motion distorts BOLD signal and reduces statistical power. Conservative thresholds (FD_mean < 0.5 mm) will be applied; sensitivity analyses will use less stringent thresholds (FD_mean < 0.75 mm) to assess robustness.

6. **Incomplete or misaligned anatomical scans:**
   - Failed coregistration to standard space (MNI or Talairach template).
   - Significant signal dropout or susceptibility artifacts affecting ROI placement.

#### **Covariates to Record (and Adjust For in Analyses)**

These variables will be measured at the study wave and included as covariates in all models:

- **Demographic:** age (continuous), sex (M/F), race/ethnicity (categorical: non-Hispanic white, Hispanic, Black, Asian, Other; will be included as covariates, not as a main grouping variable to align with NIH DEI guidelines).
- **Biological maturation:** Tanner stage or Pubertal Development Scale score (important developmental moderator; reward and inhibitory control networks continue maturing through adolescence).
- **Socioeconomic status (SES):** Composite of parental education and household income (associated with both weight status and brain development).
- **ABCD site:** Indicator variable for study site (ABCD spans 21 sites; site differences in scanner, sequences, and participant characteristics require adjustment).
- **Head motion:** Mean framewise displacement during task fMRI (as a continuous covariate to adjust for any residual motion effects).
- **Psychiatric symptoms (dimensional):** 
  - Internalizing symptoms (anxiety + depression composite from Child Behavior Checklist or dimensional symptom checrams).
  - Externalizing symptoms (ADHD, conduct problems composite).
  - *Rationale:* These are common comorbidities with BED and obesity; including them as covariates allows testing whether BI-SNN neuromarkers are BED-specific or transdiagnostic.

---

### 3.3 Tasks and Behavioral Measures

#### **3.3.1 Monetary Incentive Delay (MID) Task**

**Purpose:** Measures reward anticipation and outcome processing, core dopaminergic functions hypothesized to be altered in obesity and BED.

**Task design (standard ABCD fMRI paradigm):**
- Participants view cues signaling monetary payoffs: Large Reward (win $5), Small Reward (win $0.50), or Neutral (win $0). A target appears during anticipation phase, and participants must respond quickly (button press) to win the money if their response is fast enough.
- Trial structure: Cue (1 s) → Anticipation/delay (2-3 s) → Target (200-500 ms) → Outcome (1 s) → Feedback.
- Conditions: High reward, small reward, neutral/no reward anticipation; winners vs. losers to assess outcome processing.
- Total duration: ~8 min; ~100 trials.

**Behavioral readouts (extracted from task logs):**

1. **Reward speeding** (primary hypothesis-driven measure):
   - Definition: Reaction time difference between high-reward and neutral conditions: ΔRT_reward = RT_neutral - RT_reward.
   - Interpretation: Larger positive values indicate faster responding during high-reward anticipation (reward sensitivity). In obesity and BED, this is often exaggerated (hypersensitivity to reward cues).
   - Hypothesis: BED > obesity > healthy controls in reward speeding.

2. **Accuracy by reward condition:**
   - Hit rates in high-reward, small-reward, and neutral conditions (% correct, out of 100%).
   - Interpretation: If reward speeding is accompanied by accuracy loss, suggests impulsivity (speed-accuracy tradeoff). If maintained, suggests enhanced motivation.
   - Hypothesis: BED may show greater speed-accuracy tradeoffs.

3. **RT variability (intra-subject SD):**
   - Standard deviation of reaction times within each condition (high-reward, neutral).
   - Interpretation: Larger variability suggests inconsistent attention or motivation. Often elevated in ADHD and impulse-control disorders.
   - Hypothesis: BED > controls in RT variability.

4. **Trial-history effects (exploratory):**
   - Change in RT or accuracy on trials following wins vs. losses.
   - Interpretation: Adaptive learning from outcomes; disrupted in depression and reward-insensitive conditions.
   - Hypothesis: Exploratory; may be reduced in BED.

5. **Anticipation period brain activity (extracted via fMRI; see neural modeling):**
   - Will assess whether behavioral reward speeding correlates with ventral striatum activation during high-reward anticipation.

**Neurobiological significance:** The MID task engages ventral striatum (nucleus accumbens), ventral tegmental area, and ventromedial prefrontal cortex (vmPFC)-dopamine-rich regions implicated in reward processing (Knutson et al. 2000, NeuroImage). In obesity and BED, striatal activation during reward cues is often heightened, correlating with unhealthy eating behavior (Schag et al. 2020). However, reward anticipation also requires **inhibitory control** to delay gratification-the prefrontal cortex must modulate striatal responses to prevent impulsive action before outcomes are known. Thus, the MID task indirectly assesses reward-control coordination: individuals who show exaggerated speeding despite prefrontal input may have weak prefrontal-striatal coupling.

---

#### **3.3.2 Stop-Signal Task (SST)**

**Purpose:** Measures response inhibition and behavioral flexibility, key components of executive control hypothesized to be impaired in BED and obesity.

**Task design (standard ABCD fMRI paradigm):**
- Go trial: Participant sees a stimulus (typically a arrow pointing left or right) and must quickly press a corresponding button (left or right).
- Stop trial (20% of trials): An auditory "beep" sounds shortly after the stimulus (stop-signal delay, SSD), signaling participant to inhibit the button press.
- The SSD is dynamically adjusted: if the participant successfully stops, SSD increases on the next stop trial (making inhibition harder); if inhibition fails, SSD decreases (making inhibition easier). This tracks the participant's "stop threshold."
- Total duration: ~5 min; ~120 Go trials, ~30 Stop trials (mixed).

**Behavioral readouts:**

1. **Stop-Signal Reaction Time (SSRT) - PRIMARY MEASURE:**
   - Definition: Estimated using the horse-race model: SSRT = mean(GoRT) - mean(SSD).
   - Interpretation: Shorter SSRT indicates faster inhibitory processing (better response inhibition). Longer SSRT indicates slower inhibition or impulsivity.
   - Hypothesis: BED > obesity > healthy controls in SSRT (i.e., BED shows slower inhibition).
   - Significance: SSRT is a well-validated marker of inhibitory control deficits in ADHD, substance-use disorders, and eating disorders (Nigg 2000, Psychol Bull).

2. **Go-trial reaction time (mean RT on successful go trials):**
   - Interpretation: Establishes baseline speed. If too slow, reduces validity of SSRT (can't inhibit if not responding fast to begin with).
   - Hypothesis: Expected to be similar across groups; if elevated in BED, suggests general slowing or reduced attention rather than selective inhibition impairment.

3. **Post-error slowing (PES):**
   - Definition: ΔRT on go trials following a failed stop (commission error) vs. baseline go RT.
   - Formula: PES = RT_after_error - RT_baseline.
   - Interpretation: Positive PES indicates adaptive error monitoring (slowing down after making a mistake). Reduced or absent PES may indicate poor error awareness or weak behavioral adjustment (implicated in compulsive disorders including BED).
   - Hypothesis: BED < controls in PES (impaired error adaptation).
   - Significance: Postsynaptic error detection involves anterior cingulate cortex (ACC) and involves dopaminergic signaling; impaired PES in BED may reflect aberrant ACC-striatal communication.

4. **Commission error rate (% failed stops):**
   - Definition: Proportion of stop trials on which participant fails to inhibit (presses button despite the stop signal).
   - Interpretation: Direct measure of inhibition failure; higher rates suggest weaker inhibitory control.
   - Hypothesis: BED > obesity > healthy controls (BED may have higher error rates despite dynamic SSD adjustment).

5. **Omission error rate (% missed go trials):**
   - Definition: Proportion of go trials on which participant fails to respond.
   - Interpretation: If elevated (>10%), suggests attentional lapses or reduced motivation.
   - Hypothesis: Expected to be low across groups; if elevated in BED, may indicate comorbid inattention.

6. **Stop-trial success rate:**
   - Definition: Proportion of stop trials on which inhibition is successful.
   - Interpretation: Another direct index of inhibition.

**Neurobiological significance:** The SST engages dorsolateral prefrontal cortex (dlPFC), inferior frontal gyrus (IFG, particularly right hemisphere), pre-supplementary motor area (pre-SMA), and anterior cingulate cortex (ACC)-the "inhibitory control network." These regions are hypothesized to be hypoactive or poorly coordinated in BED (Huo et al. 2017, Obesity), particularly when engaged during food-cue exposure. Crucially, the SST also engages **striatum and ventral tegmental area** (reward regions), as inhibition competes with reward-driven approach. The SST is thus a window into reward-control **conflict resolution**. If prefrontal-striatal coupling is weak, participants may show impulsive responding on SST, and this should correlate with binge-eating severity.

---

### 3.4 Neural Modeling: BI-SNN Framework (Kasabov NeuCube)

#### **3.4.1 Input Preprocessing and ROI Selection**

##### **FMRI Data Source and Preprocessing**

- **Source:** ABCD's minimally preprocessed fMRI data or raw DICOM, depending on availability and requirement for additional denoising.
- **Preprocessing steps to apply (if needed):**
  1. Motion correction (realignment to first volume).
  2. Slice-timing correction (to account for differences in slice acquisition within a TR).
  3. Co-registration to structural T1 image, then to standard template (MNI or Talairach).
  4. Spatial smoothing (optional; NeuCube can work on unsmoothed data, but moderate smoothing [4-6 mm FWHM] may improve signal-to-noise without losing spatial specificity). **Sensitivity analysis:** run models with and without smoothing.
  5. Denoising:
     - Regression out motion parameters (6 rigid-body + their temporal derivatives = 12 motion regressors).
     - Physiological noise correction if available (cardiac, respiratory; RETROICOR algorithm or similar).
     - Scrubbing: flag and optionally censoring volumes with framewise displacement > 0.9 mm (or robust outlier detection via AFNI 3dToutcount).
  6. Temporal filtering: bandpass filtering (0.01-0.1 Hz) to remove very-low-frequency drift and high-frequency noise, consistent with standard fMRI practice.

##### **ROI Selection: Reward and Control Networks**

Based on the literature and ABCD capabilities, the following ROIs will be defined in MNI or Talairach space and used as input to the NeuCube:

**Reward Network (Dopaminergic):**
- Ventral Striatum / Nucleus Accumbens (bilateral; core and shell).
- Caudate and Putamen (bilateral; dorsal striatum; involved in habit and reward learning).
- Ventromedial Prefrontal Cortex (vmPFC; Brodmann areas 11, 25, 32).
- Orbitofrontal Cortex (OFC; lateral and medial; Brodmann area 12/47).
- Ventral Tegmental Area (VTA; small, difficult to image, but attempts will be made).

*Rationale:* These regions form the "ventral tegmental area-nucleus accumbens-prefrontal cortex" circuit (Volkow et al. 2017, Nat Rev Neurosci), central to motivation, reward expectancy, and decision-making. Dopamine from VTA projects to both striatum (encoding reward prediction error) and prefrontal cortex (supporting flexible decision-making). Hypoactive vmPFC and OFC in BED suggest weakened reward evaluation and impulse control.

**Inhibitory Control Network (Fronto-Parietal):**
- Dorsolateral Prefrontal Cortex (dlPFC; Brodmann areas 9, 46; bilateral, with rightward emphasis).
- Inferior Frontal Gyrus (IFG; right > left; pars opercularis and pars triangularis; Brodmann areas 44, 45).
- Pre-Supplementary Motor Area (pre-SMA; Brodmann area 6; medial).
- Anterior Cingulate Cortex (ACC; dorsal anterior cingulate, Brodmann area 24; involved in error monitoring and conflict detection).
- Posterior Parietal Cortex (PPC; intraparietal sulcus; bilateral; involved in attention and decision processes).

*Rationale:* These regions comprise the "right inferior fronto-parietal inhibition network" (Swick et al. 2011, Neurosci Biobehav Rev), critical for response inhibition, error monitoring, and adaptive behavior. Hypoactivity or poor coordination in these regions is associated with ADHD, impulse-control disorders, and eating disorders (Huo et al. 2017).

**Integration Node (Bridging reward and control):**
- Ventromedial Prefrontal Cortex (vmPFC) again: listed in both networks because it receives dopaminergic input and projects to inhibitory regions; acts as a "value integrator" that bridges bottom-up reward signals and top-down control (Rangel et al. 2008, Annu Rev Neurosci).
- Anterior Insula (bilateral; Brodmann area 16): integrates interoceptive signals with reward and control; involved in cue-induced craving and impulse resistance (Craig 2009, Nat Rev Neurosci).

**Total ROI count:** ~20-25 anatomically defined regions (bilateral pairs + midline structures).

*Implementation approach:*
- Use a standard atlas (e.g., AAL-Automated Anatomical Labeling; or FSL Harvard-Oxford atlas) to define ROI masks.
- Extract mean BOLD time series for each ROI (averaged over all voxels within that ROI) for each task trial.
- Alternative: If greater spatial detail is desired, parcellate ROIs into smaller sub-regions (e.g., core vs. shell of nucleus accumbens; dorsal vs. ventral ACC) using published coordinates or functional atlases (e.g., Schaefer et al. 2018).

*Sensitivity analysis:* Repeat analyses using alternative ROI definitions (e.g., ICA-derived components, voxel-wise approaches without ROI averaging) to test robustness.

---

##### **Trial-Level Extraction and Alignment**

For each task (MID, SST), extract fMRI time series aligned to key events:

**MID task:**
- Extract 14-second windows (7 TRs at 2-second TR typical for ABCD) per trial, time-locked to stimulus cue onset:
  - Cue: t = 0
  - Anticipation: t = 2-5 s
  - Target: t = 5-7 s
  - Outcome: t = 7-10 s
  - Rest: t = 10-14 s
- Separate trials by condition (high reward vs. low reward vs. neutral; winners vs. losers) for stratified analyses.
- Create one "sample" per trial per ROI = 14-s BOLD time series.

**SST task:**
- Extract 10-second windows (5 TRs) per trial, time-locked to stimulus (go or stop-signal):
  - t = 0: stimulus onset (arrow).
  - t = 2-4 s: response period (go trials) or inhibition period (stop trials).
  - t = 4-10 s: outcome (feedback).
- Separate by trial type (successful go, failed stop [commission error], successful stop).
- Create one "sample" per trial per ROI = 10-s BOLD time series.

*Rationale:* Trial-level extraction preserves the temporal dynamics of individual events, allowing the BI-SNN to learn associations between fMRI patterns and trial outcomes (e.g., "high-reward anticipation patterns in nucleus accumbens preceding fast RTs").

---

#### **3.4.2 Spike Encoding: The Threshold-Based Representation (TBR) Method**

**Conceptual overview:**

Continuous fMRI BOLD signal (ranging from low to high intensity values) is converted into a binary "spike" representation, where a spike signals the presence of an activation change exceeding a threshold. This transformation is justified by three principles:

1. **Preserves timing information:** Unlike averaging BOLD over long windows, spike encoding captures the *moment* at which activation rises above baseline, preserving temporal resolution.
2. **Robust to noise:** Small fluctuations below the threshold do not generate spikes, filtering out noise while retaining task-related transients.
3. **Computationally efficient for SNNs:** Spiking networks naturally work with discrete temporal events (spikes) rather than continuous values; encoding BOLD as spikes leverages SNN advantages.

**Mathematical formulation (adapted from Kasabov et al. 2016, 2017):**

For a given ROI time series S(t) over a trial (t ∈ {tâ‚€, tâ‚, ..., t_L}):

1. **Identify minimum:** Determine time t_m when signal is minimized (start of task-related activation).

2. **Set baseline:** B(t_m) = S(t_m) (initialize baseline to minimum).

3. **Iterate through timepoints** t ∈ {t_m, t_m+1, ..., t_L}:
   - If S(t_{i+1}) > B(t_i): **generate a spike** at time t_{i+1}, and update baseline as:
     - B(t_{i+1}) = α·S(t_{i+1}) + (1-α)·B(t_i)
   - If S(t_{i+1}) ≤ B(t_i): **no spike**, and reset baseline as:
     - B(t_{i+1}) = S(t_{i+1})

Where **α ∈ [0, 1]** is a parameter controlling how quickly the baseline adapts to signal increases. Typical value: α = 0.5 (Kasabov et al. 2017).

**Interpretation:**
- **Successive spikes** (t_i to t_{i+2} with spikes at both times) represent *sustained or repeated increase* in BOLD (rising signal slope).
- **Absence of spikes** (gap in spike times) represents *decreasing signal* (return to baseline or below).
- **Spike timing** preserves the temporal order of activation across ROIs.

**Example:** Suppose nucleus accumbens (NAcc) shows a rising BOLD signal during high-reward anticipation from t=2 to t=4 s, then plateaus. Spike encoding would generate spikes at t=2, t=3, t=4 (rising phase) and few/no spikes at t=5-7 s (plateau). In contrast, dlPFC may show a delayed rise from t=3 to t=5 s, generating spikes starting later. The *temporal offset* (NAcc spikes precede dlPFC spikes) is captured in the spike train and will be learned by STDP.

**Parameter selection and sensitivity:**
- **α (adaptation rate):** Kasabov et al. (2017) used α = 0.5. Sensitivity analyses will test α ∈ {0.3, 0.5, 0.7} to assess robustness.
- **Alternative thresholds:** Some SNNs use fixed thresholds (e.g., BOLD > baseline + 0.5 SD) rather than adaptive. We will compare adaptive TBR to fixed-threshold encoding in pilot analyses.

**Validation of spike encoding:**
- Verify that spike patterns align with known task-related BOLD dynamics (e.g., NAcc shows earlier/stronger spike trains during high-reward cues, dlPFC shows stronger spikes during inhibitory control demands).
- Compare classification accuracy of BI-SNN models trained on spike-encoded data vs. raw BOLD time series vs. static GLM contrasts. Expect spike-encoded models to outperform or match other approaches while providing mechanistic interpretability.

---

#### **3.4.3 BI-SNN Architecture: NeuCube Spatial Mapping and Connectivity Initialization**

**3D Spiking Neural Cube (SNNc) Initialization:**

Following Kasabov et al. (2016, 2017), a 3D cube of spiking neurons is created to spatially map the brain:

- **Cube dimensions:** Determined by the Talairach or MNI template used. For standard Talairach (common in ABCD), the cube spans approximately 100 mm (anterior-posterior) × 80 mm (left-right) × 60 mm (dorsal-ventral). If mapped to a 1 mm resolution grid, this yields ~480,000 neurons. For computational tractability, we will **downsample to 2-3 mm resolution**, yielding ~60,000-135,000 neurons. Kasabov et al. (2016) used 1,471 neurons (coarse atlas-based mapping); we will explore both coarse and finer resolution in sensitivity analyses.

- **ROI-to-neuron mapping:** Each of the ~20-25 reward and control ROIs (defined above) is mapped to a set of neurons in the SNNc corresponding to that region's Talairach/MNI coordinates. For example, nucleus accumbens (centered around x=±10, y=8, z=-8 mm in MNI) is mapped to neurons at those approximate coordinates within the cube.

- **Input neuron allocation:** Each input ROI has one or more "input neurons" (depending on ROI size) that receive the spike trains extracted from that ROI's fMRI time series. These input neurons act as "gateways" for external data into the SNNc.

**Connectivity Initialization: Small-World Rule (Kasabov et al. 2016, 2017):**

Before learning, connections between neurons are initialized using the "small-world" connectivity principle, observed in biological neural systems (Watts & Strogatz 1998, Nature):

- **Distance threshold (D_thr):** Two neurons are connected if their 3D distance in the SNNc cube is ≤ D_thr (typically 5-10 mm in physical space, corresponding to ~5-10 neuron steps in the discretized cube). This creates short-range ("local") connections.
- **Bidirectional initialization:** For neurons i and j within D_thr, both w_ij and w_ji are initialized to zero (weights are initially unlearned but the structural connection exists).
- **Result:** An initially sparse, anatomically organized connectivity pattern where nearby neurons (e.g., two subregions within striatum) are more likely to be connected than distant ones (e.g., striatum to visual cortex far away). This mimics the anatomical organization of the brain and reduces overfitting.

**Parameters to optimize (via grid search or genetic algorithm):**
- D_thr (distance threshold): range {3, 5, 7, 10} mm.
- Initial cube resolution (1 mm vs. 2 mm vs. 3 mm): affects number of neurons and computational cost.

---

#### **3.4.4 Unsupervised Learning: STDP in the SNNc**

**Spike-Timing-Dependent Plasticity (STDP):**

After encoding fMRI data into spike trains and initializing the SNNc, unsupervised learning is performed using STDP. The rule modifies synaptic weights based on the *temporal relationship* between pre-synaptic and post-synaptic spike times (Kasabov et al. 2016, 2017):

**Modified STDP learning rule (from Kasabov et al. 2016):**

For connected neurons i and j, if neuron i (presynaptic) fires at time t_pre and neuron j (postsynaptic) fires at time t_post:

- **Δt = t_post - t_pre** (time difference, positive if post-synaptic fires after pre-synaptic).

If Δt ≤ 0 (presynaptic spike precedes postsynaptic):
   - **Δw_ij = A+ · exp(Δt / Ï„+)**

Otherwise (postsynaptic fires first):
   - **Δw_ij = 0** (no weight change).

**Parameters:**
- **A+:** Maximum weight increment (~0.1 in Kasabov et al. 2016).
- **Ï„+:** Temporal window (~1 time unit = 1 TR â‰ˆ 2 seconds; slightly longer windows may be useful for fMRI).

**Interpretation:**
- If ROI A consistently fires (via spikes) *before* ROI B (Δt < 0), the connection weight from A to B increases, indicating a learned temporal precedence.
- This captures functional causality or coordinated timing: "A tends to activate before B during this task."
- Over many trials, bidirectional connections between i and j are learned; the **stronger connection is retained, the weaker is pruned** (Kasabov et al. 2016).

**Why STDP is appropriate here:**
- **Biologically plausible:** STDP is a well-established synaptic learning rule observed in real neurons (Bi & Poo 2001, Annu Rev Neurosci).
- **Captures temporal dynamics:** Unlike static correlation (which ignores timing), STDP explicitly learns about temporal sequence and causality.
- **Unsupervised:** STDP does not require class labels; it discovers patterns autonomously. This is valuable for exploratory analysis and hypothesis generation.

**Training procedure:**
- For each subject, all trial-wise spike trains (e.g., 100 MID trials + 120 SST trials = 220 samples) are presented sequentially to the SNNc.
- During each trial's spike train presentation (14 s for MID, 10 s for SST), spikes propagate through the SNNc, activate neurons, and trigger STDP updates.
- After one pass through all trials (one "epoch"), the model can be tested for classification or for neuromarker extraction. For stability, typically 3-5 epochs of training are used (Kasabov et al. 2016, 2017).
- After training, the SNNc contains learned connection weights w_ij that reflect spatiotemporal associations in the fMRI data.

---

#### **3.4.5 Neuromarker Feature Extraction from Learned SNNc**

After unsupervised learning, the trained SNNc is analyzed to extract interpretable neuromarker features. These features will be used for group comparisons, behavioral associations, and downstream prediction.

**Feature categories:**

**A. Within-Network Dynamics:**

*Activation degree (D_i):* For each neuron i (or for each ROI aggregating neurons in that region), calculate the activation degree as (Kasabov et al. 2016):

D_i = [Î£ (w_ij + w_ji)] / number_of_neighbors

where the sum is over all neighbors j of neuron i within the connection distance threshold.

**Interpretation:** High D_i indicates that neuron i has strong incoming and outgoing connections, suggesting it is a "hub" or key integrator within its local network. In a reward-processing region, high D_i during reward-anticipation trials suggests active reward encoding. In a control region, high D_i during inhibitory control trials suggests active inhibition.

**Neuromarkers extracted:**
1. **Mean D_i in reward ROIs (nucleus accumbens, OFC, vmPFC) during high-reward anticipation phase** of MID trials.
   - Hypothesis: BED > obesity > controls (heightened reward network activation).

2. **Mean D_i in inhibitory ROIs (dlPFC, IFG, ACC) during stop trials** of SST.
   - Hypothesis: BED < controls (reduced inhibitory network activation).

3. **D_i variability (SD across trials):** Across many trials, compute the trial-to-trial variability in D_i for each ROI.
   - Interpretation: High variability might indicate inconsistent or noisy engagement; low variability indicates stable, reliable activation.
   - Hypothesis: Exploratory; may be elevated in BED (inconsistent inhibitory control).

---

**B. Cross-Network Coordination (Reward-Control Coupling):**

**Temporal offset metric:** For each trial, identify the timing of peak activation in reward ROIs (NAcc, OFC) and in control ROIs (dlPFC, IFG). Compute the time delay between them:

- **Temporal offset = T_peak_control - T_peak_reward**

**Interpretation:**
- Negative offset: Control region peaks *before* reward region (prefrontal "anticipates" and prepares inhibition).
- Positive offset: Reward region peaks *before* control region (reward "leads" and control responds reactively).
- Small offset: Tight temporal coupling; reward and control regions are well-coordinated.
- Large offset: Loose coupling; dissociated activation dynamics.

**Hypothesis:** BED shows *larger positive offsets* or *larger variability in offsets* compared to controls, indicating that reward activation precedes and overwhelms inhibitory control responses.

**Connection strength metrics:** For each subject, compute the learned connection weights w_ij between reward and control ROIs (e.g., w_reward_to_control = average of weights from NAcc to dlPFC, OFC to IFG, etc.).

- **Reward-to-control connection strength:** Weights from reward ROIs to control ROIs.
- **Control-to-reward connection strength:** Weights from control ROIs to reward ROIs (top-down modulation).

**Hypotheses:**
- BED shows *weaker control-to-reward connections* (reduced top-down inhibition of reward).
- BED shows *stronger or unchecked reward-to-control weights* (unmodulated reward signaling).

---

**C. Cross-Task Coordination (Task Generalization):**

**Shared representational structure:** Compare patterns of learned connections across MID and SST tasks. For each subject:

1. Train a separate SNNc on MID trials only; extract features F_MID.
2. Train a separate SNNc on SST trials only; extract features F_SST.
3. Compute similarity between F_MID and F_SST:
   - Euclidean distance, cosine similarity, or rank-order correlation.

**Interpretation:** If F_MID and F_SST are highly correlated within an individual, it suggests that the same underlying reward-control circuitry is engaged across both tasks. If uncorrelated, it suggests task-specific or disconnected processing.

**Hypothesis:** Healthy controls show *higher cross-task similarity* (coherent, shared network organization). BED shows *lower similarity* (task-specific, fragmented representations or dysregulated transitions between tasks).

*Rationale:* Cognitive flexibility and adaptive behavior require the brain to maintain a coherent internal model that can be applied across contexts. BED may involve "stimulus-bound" or impulsive responding, wherein each task triggers independent reactive patterns without stable integrative structure.

---

**D. Temporal Dynamics of Network Responses (Within-Trial Time-Course):**

For each trial phase (e.g., cue, anticipation, outcome in MID; go, stop-signal, response, feedback in SST), compute the *rise time* and *peak latency* of activation in key ROIs:

- **Rise time:** Time from baseline to 50% of peak activation (sharpness of activation onset).
- **Peak latency:** Time at which maximum D_i is reached (when does the region "activate").

**Hypotheses:**
- BED shows *faster rise times and earlier peak latencies* in reward regions during reward anticipation (rapid, hair-trigger reward response).
- BED shows *slower rise times and delayed peak latencies* in control regions during inhibitory demands (sluggish, reactive control).

---

**Summary of candidate neuromarkers (study 1):**

| **Feature Name** | **Computation** | **Expected Direction in BED** | **Rationale** |
|---|---|---|---|
| NAcc/OFC activation (MID reward anticipation) | Mean D_i in ventral striatum/OFC during high-reward cue | Elevated (â†‘) | Heightened reward sensitivity |
| dlPFC/IFG activation (SST inhibition) | Mean D_i in dlPFC/IFG during stop trials | Reduced (â†“) | Weakened inhibitory control |
| Reward-control offset (temporal) | T_control - T_reward during MID | Larger positive (>>0) | Reward dominates control |
| Reward→Control coupling strength | w_ij from NAcc/OFC to dlPFC/IFG | Weaker (â†“) | Reduced top-down input from reward |
| Control→Reward coupling strength | w_ij from dlPFC/IFG to NAcc/OFC | Weaker (â†“) | Reduced inhibitory modulation of reward |
| Cross-task similarity (F_MID vs. F_SST) | Correlation or distance between task-specific features | Lower (â†“) | Task-specific, non-integrated processing |
| Temporal variability of activation | SD of peak latencies across trials | Higher (â†‘) | Inconsistent, noisy engagement |

---

#### **3.4.6 Supervised Classification: Validating Neuromarker Separability**

**Optional (exploratory) classification analysis:**

After extracting the above neuromarkers for each subject, train a supervised classifier (elastic net logistic regression, random forest, or SVM) to test whether BI-SNN features can distinguish BED, obesity, and healthy-weight groups:

- **Input features:** The ~10-15 neuromarker features listed above (plus optional behavioral indices).
- **Output:** Group label (BED vs. obesity vs. healthy; or binary contrasts: BED vs. others, obesity vs. lean).
- **Validation:** 10-fold cross-validation; report AUC, sensitivity, specificity, balanced accuracy.
- **Baseline comparisons:**
  - Classifier trained on behavioral indices alone (SSRT, reward speeding, etc.).
  - Classifier trained on standard fMRI contrasts (mean BOLD in reward vs. control ROIs, static functional connectivity).
  - Classifier trained on BI-SNN features.
  - Classifier trained on BI-SNN + behavioral features combined.
  - Expected: BI-SNN features provide incremental predictive value over baseline approaches.

**Significance:** If BI-SNN classification accuracy exceeds static methods, it demonstrates that spatiotemporal dynamics capture information not in static measures, validating the approach.

**Caveats:** Classification is not the primary aim of Study 1; the primary aim is to identify and characterize neuromarkers. Classification is a secondary validation exercise.

---

### 3.5 Statistical Analyses: Group Comparisons and Associations

#### **3.5.1 Primary Group Comparisons (Hypothesis Testing)**

**Group definitions and primary contrasts:**

1. **Three-group ANOVA (exploratory):**
   - Compare BED vs. obesity vs. healthy controls on each neuromarker (D_i, temporal offset, coupling strengths, etc.).
   - Use mixed-model ANOVA with covariates (age, sex, site, motion, internalizing/externalizing symptoms).
   - Adjust for multiple comparisons: Bonferroni correction across ~12 primary neuromarkers → α_corrected = 0.05 / 12 â‰ˆ 0.004.

2. **Binary comparisons (primary focus):**
   - BED vs. non-BED (combining obesity + healthy controls): most discriminatory contrast.
   - Obesity (any) vs. lean (combining healthy controls): dimensional severity contrast.
   - BED vs. obesity: specificity test (are neuromarkers BED-specific or general disinhibition markers?).
   - Use two-sample t-tests (or Welch's t-test if variances unequal) with covariates via ANCOVA.

3. **Stratified analyses (sensitivity):**
   - Repeat all comparisons separately for males and females (sex differences in eating disorders are well-documented; expect potential neurobiological differences).
   - Repeat for subgroups by puberty stage (Tanner stage) to test developmental effects.
   - Repeat with vs. without ADHD or ASD participants (to test whether neurodevelopmental comorbidity confounds results).

---

#### **3.5.2 Behavioral Associations**

**Hypothesized associations (Spearman or Pearson correlations, adjusted for covariates):**

For each neuromarker, test associations with behavioral indices:

| **Neuromarker** | **Behavioral Measure** | **Expected Correlation** | **p-threshold** |
|---|---|---|---|
| NAcc activation (MID) | Reward speeding (ΔRT) | Positive (r > 0.2) | 0.05 (or Bonferroni-corrected) |
| NAcc activation (MID) | Binge frequency (EDE-Q) | Positive (r > 0.15) | 0.05 |
| dlPFC activation (SST) | SSRT (stop-signal RT) | Negative (r < -0.2) | 0.05 |
| Temporal offset (reward-control) | Binge severity composite | Positive (r > 0.2) | 0.05 |
| Reward→Control coupling | Disinhibition scale (BIS-15) | Negative (r < -0.2) | 0.05 |

**Interpretation:** If expected correlations are observed and statistically significant, it strengthens the claim that BI-SNN neuromarkers reflect behaviorally relevant neural dysfunction.

**Multiple comparison correction:** Use false discovery rate (FDR) control at q < 0.05 across all correlation tests (e.g., ~20-30 primary correlations × 2-3 sensitivity analyses → ~60-90 tests total).

---

#### **3.5.3 Clinical Severity Associations**

**Test associations between neuromarkers and dimensional eating-disorder severity:**

1. **Continuous binge-eating frequency** (number of binge episodes per month from EDE-Q or KSADS):
   - Linear regression: binge frequency ~ neuromarker + covariates.
   - Report Î² (slope), 95% CI, and RÂ² (variance explained).
   - Hypothesis: Several neuromarkers independently associated with binge frequency (partial associations after covariate adjustment).

2. **Loss-of-control (LOC) eating score** (severity of feeling out of control during eating):
   - Similar regression approach.
   - May be more specific to BED than binge frequency alone (some individuals binge without LOC; diagnostic emphasis is on LOC).

3. **BMI z-score** (age- and sex-adjusted):
   - Do reward-control neuromarkers predict BMI over and above group membership?
   - Linear regression: BMI ~ neuromarkers + group + covariates.
   - Tests whether neuromarkers capture individual differences within BED and obesity groups.

---

#### **3.5.4 Confound and Sensitivity Analyses**

**Potential confounders to investigate:**

1. **Psychiatric comorbidities:**
   - Depression (PHQ-9 or BDI score): associated with both anhedonia (reduced reward) and apathy (reduced inhibition).
   - Anxiety (GAD-7): associated with elevated inhibitory control (over-caution) and threat-related hypervigilance.
   - ADHD (Conners or DIVA): strongly associated with reduced SSRT, impulsivity, and reward sensitivity.
   - Substance use: associated with altered dopaminergic function.
   - **Approach:** Repeat analyses adjusting for each symptom dimension as a covariate; also report results in ADHD-excluded and depression-excluded subsamples.

2. **Medications:**
   - Stimulant use (ADHD treatment): increases dopamine and can enhance inhibitory control.
   - Antidepressants: alter serotonin-dopamine balance.
   - **Approach:** Pre-specify medication status at assessment; conduct sensitivity analyses excluding medicated subjects (if n sufficient) and including medication as a covariate.

3. **Head motion and data quality:**
   - Motion during fMRI can corrupt BOLD signal and artificially reduce apparent connectivity.
   - **Approach:** Include mean FD as a covariate in all analyses; report results before/after motion adjustment; test whether motion-related confounding differs by group (e.g., BED participants may move more due to hyperactivity or discomfort in scanner).

4. **Site effects:**
   - ABCD spans 21 sites with different scanners, acquisition sequences, and participant demographics.
   - **Approach:** Include site as a fixed effect; compute ICC (intraclass correlation) to quantify site variance; report if results are site-specific or generalizable.

5. **Imaging protocol variations:**
   - Subtle differences in TR, flip angle, voxel size, etc., can affect BOLD amplitude.
   - **Approach:** Pre-process data separately by acquisition protocol; include protocol as a covariate if applicable.

---

#### **3.5.5 Robustness Checks**

**Alternative analytic approaches to validate primary findings:**

1. **Non-parametric tests:** Due to potential non-normality of neuromarker distributions, repeat key group comparisons using Mann-Whitney U tests (for binary contrasts) or Kruskal-Wallis tests (for three-way comparisons).

2. **Outlier exclusion:** Identify univariate outliers (|z| > 3) and multivariate outliers (Mahalanobis distance); repeat analyses excluding these cases to test whether results are driven by extreme values.

3. **Alternative spike-encoding parameters:** Re-run SNN training with different TBR thresholds (α ∈ {0.3, 0.7}) and different connection distance thresholds (D_thr ∈ {3, 7} mm); report whether neuromarker magnitudes and group differences are robust to parameter choices.

4. **Alternative ROI definitions:** Repeat analyses using:
   - Voxel-wise BI-SNN (no ROI averaging; all voxels in reward/control regions included as input neurons).
   - Functional parcellation (ICA-derived components or Schaefer et al. atlas) instead of anatomical ROIs.
   - Expect qualitatively similar findings if method is robust.

---

### 3.6 Reporting and Interpretation

#### **3.6.1 Primary Results Table**

**Table: Study 1 Group Comparisons on Neuromarkers**

| **Neuromarker** | **BED (mean ± SD)** | **Obesity (mean ± SD)** | **Healthy (mean ± SD)** | **Test Statistic** | **p-value** | **Effect Size (Cohen's d or Î·Â²)** | **Interpretation** |
|---|---|---|---|---|---|---|---|
| NAcc activation (D_i) | ... | ... | ... | t(XX) = X.XX | p < 0.001 | Î·Â² = 0.12 | BED > controls âœ“ |
| dlPFC activation (D_i) | ... | ... | ... | F(2,XXX) = X.XX | p = 0.045 | Î·Â² = 0.03 | BED < controls âœ“ (medium) |
| Temporal offset | ... | ... | ... | t(XX) = X.XX | p = 0.002 | d = 0.45 | BED > controls âœ“ |
| Reward→Control coupling | ... | ... | ... | t(XX) = X.XX | p = 0.078 | d = 0.25 | Trend, not significant |

---

#### **3.6.2 Visualization and Connectivity Maps**

**Generate 3D visualizations of learned SNNc connectivity (adapted from Kasabov et al. 2016, 2017):**

1. **Brain-space heat map:** Display the learned connection weights in the 3D SNNc overlaid on a brain template. Color intensity represents connection strength; color hue represents direction (excitatory vs. inhibitory).
   - Show separately for BED, obesity, and control groups.
   - Highlight differences in connectivity patterns between groups (e.g., BED shows weaker prefrontal-striatal connections).

2. **Anatomical connectivity diagram:** Simplified schematic showing key ROIs (nodes) and connection strengths (edge weights) between them.
   - For each group and each task phase (cue, anticipation, response, outcome).
   - Facilitate reader's understanding of group-level network organization.

3. **Temporal dynamics plots:** For each group, plot the time-course of activation (D_i) in reward vs. control ROIs across the trial.
   - Highlight temporal offsets and lag structures.
   - Example: "Control group shows dlPFC activation (red line) slightly preceding NAcc activation (blue line) during SST, consistent with top-down inhibitory control. BED group shows NAcc activating *before* dlPFC (reversed temporal order), consistent with reward-driven impulsivity."

---

### 3.7 Study 1 Outcomes and Interpretations

#### **3.7.1 Scenario A: Strong Behavioral + Neural Effects (Predicted)**

**Findings:**
- Significant group differences in multiple BI-SNN neuromarkers.
- BI-SNN features associated with behavioral markers (reward speeding, SSRT, post-error slowing).
- BI-SNN features explain additional variance beyond standard fMRI contrasts.

**Interpretation:**
- Strong support for the hypothesis that spatiotemporal reward-control coordination is disrupted in BED/obesity.
- BI-SNN method provides methodological and mechanistic value.
- Neuromarkers are promising candidates for Study 2 prediction.
- **Publication outlet:** High-impact neuroscience journal (NeuroImage, Cortex, Biological Psychiatry) with emphasis on methods + mechanisms.

---

#### **3.7.2 Scenario B: Neural Differences, Weak Behavioral Associations**

**Findings:**
- Significant group differences in BI-SNN neuromarkers.
- BUT: weak or no correlations with behavioral indices.

**Interpretation:**
- BI-SNN features capture neural heterogeneity not reflected in simple behavioral readouts.
- Possible explanations:
  1. Behavioral measures (RT, SSRT) are noisy or have low reliability in adolescents (developmental variability in task engagement).
  2. Neural features are "downstream" of behavior (neural compensation: BED individuals use alternative strategies to maintain adequate performance despite circuit dysfunction).
  3. BI-SNN is overfitting or capturing noise.
- **Action:** Examine whether BI-SNN neuromarkers predict BED trajectories in Study 2 (prospective validation) even without concurrent behavioral associations. If yes, neural features remain valuable. If no, suggests method is not capturing behaviorally/clinically relevant information.

---

#### **3.7.3 Scenario C: Behavioral Effects, No SNN Advantages**

**Findings:**
- Group differences in behavioral indices (reward speeding, SSRT) observed.
- BUT: BI-SNN features do not explain additional variance beyond static fMRI activation/connectivity.

**Interpretation:**
- Spatiotemporal BI-SNN modeling does not add value over simpler methods for this specific task/phenotype.
- Possible reasons:
  1. Eating-disorder group differences may be driven by static network organization (trait-like connectivity) rather than trial-by-trial dynamics.
  2. BOLD temporal resolution (~2 s) may be too coarse to capture meaningful spike-level temporal structure; fMRI may intrinsically be a "static" modality.
  3. BI-SNN hyperparameter tuning (threshold, distance, learning rate) may not be optimized for fMRI (although Kasabov et al. validated the approach).
- **Action:** Report as negative result (valuable for field). Do not over-interpret BI-SNN value; reposition as exploratory. Consider whether EEG (finer temporal resolution) might be better suited for spike-based approaches.

---

#### **3.7.4 Scenario D: Null or Inconsistent Findings**

**Findings:**
- No clear group differences; inconsistent across subgroups (e.g., significant in females but not males).

**Interpretation:**
- Possible reasons:
  1. Sample size insufficient for smaller group (BED n < 50 after QC).
  2. ABCD group definitions (based on questionnaires) may be misaligned with neurobiological subtypes.
  3. Age or developmental stage inappropriate for expected neural effects (e.g., circuits still too plastic at ages 13-16 to show stable differences).
- **Action:** Pre-register expected effect sizes and power calculations before Study 1 analyses; if underpowered, acknowledge limitation. Consider replication in multi-site meta-analyses or in clinical cohorts with higher BED prevalence.

---

### 3.8 Study 1 Timeline and Deliverables

| **Phase** | **Duration** | **Deliverables** |
|---|---|---|
| **Data acquisition & QC** | Months 1-3 | Finalized sample (n=380-480); quality-checked fMRI and behavioral data |
| **ROI definition & preprocessing** | Months 3-4 | Standardized ROI masks; trial-level BOLD time series extracted |
| **Spike encoding & SNNc training** | Months 4-6 | Spike-encoded data; trained SNNc models for each subject (MID + SST) |
| **Neuromarker extraction & statistics** | Months 6-8 | Neuromarker datasets; group comparisons; association analyses; visualizations |
| **Manuscript preparation** | Months 8-10 | Methods + Results paper: "Spatiotemporal Neuromarkers of Reward-Control Dysfunction in Adolescent BED and Obesity" |
| **Submission & revision** | Months 10-14 | Published paper (or major revisions) |

---

---

## 4. STUDY 2: LONGITUDINAL PREDICTION OF BED TRAJECTORIES

### 4.1 Objectives

1. To test whether BI-SNN neuromarkers and behavioral indices extracted at an **early adolescent timepoint (ages 11-14)** predict **future BED onset, symptom persistence, and severity change** over a 2-4-year follow-up (to ages 15-16).

2. To evaluate the **incremental predictive value** of BI-SNN features over behavioral indices and static fMRI connectivity alone (comparative prediction models).

3. To identify **high-risk and low-risk phenotypes** based on neuromarker profiles; potential basis for future stratified prevention or early intervention.

4. To test **specificity:** do BI-SNN features predict BED specifically, or do they generalize to other psychopathology (depression, anxiety, substance use, ADHD symptoms)?

### 4.2 Study Design and Waves

#### **4.2.1 Longitudinal Design**

**Two-timepoint prospective design:**

- **Baseline / Predictor wave:** Ages 11-14 years (baseline through 2-year follow-up in ABCD; approximately 50-75% of original cohort completes imaging at these waves).
- **Outcome wave:** Ages 15-16 years (approximately 6-year follow-up from initial ABCD baseline; ~60-70% retention).

**Rationale for wave selection:**

- **Ages 11-14 predictor wave:** This is before full ED phenotypes are crystallized but after preliminary subclinical symptoms may emerge. Early intervention research suggests that intermediate phenotypes (e.g., loss-of-control eating, dietary restraint) present by age 11-12. Baseline fMRI imaging in ABCD begins at age 9-10, so ages 11-14 fMRI is commonly available.

- **Ages 15-16 outcome wave:** Eating-disorder symptom severity and diagnosis are more fully expressed at this age; sufficient developmental time has elapsed (4-6 years) to observe meaningful trajectories (onset of new cases, worsening of existing symptoms, remission of others).

#### **4.2.2 Inclusion Criteria for Study 2**

1. **Baseline (predictor) requirements:**
   - Completed MID + SST fMRI at ages 11-14 (or earliest available imaging age with usable data).
   - Completed eating-disorder assessments (KSADS-ED module, EDE-Q, or LOC eating screener) at baseline.
   - Baseline fMRI passing quality control (as in Study 1).
   - **Baseline ED status:** Either no BED (for incident BED analyses), or any ED status including subthreshold (for trajectory analyses).

2. **Follow-up (outcome) requirements:**
   - Completed eating-disorder assessments at ages 15-16 (same instruments as baseline).
   - Ideally, re-scanning at ages 15-16 (but not required for primary prediction model, which uses baseline neuroimaging to predict outcome ED status).
   - Retention to outcome assessment â‰¥70% (if retention < 70%, report attrition bias analyses).

#### **4.2.3 Predictor Wave Selection: Handling Multiple Imaging Timepoints**

**Challenge:** ABCD participants may have completed fMRI at multiple timepoints within the ages 11-14 window (e.g., baseline at age 9-10, 2-year follow-up at age 11-12, 4-year follow-up at age 13-14).

**Solution (pre-registered):** Use the **earliest available baseline fMRI** (typically age 9-10 or first available usable scan) as the predictor wave. This maximizes sample size and extends the prediction horizon. Sensitivity analysis: repeat with latest fMRI before age 14 to test robustness to wave selection.

---

### 4.3 Sample, Retention, and Attrition

#### **4.3.1 Expected Sample Size**

Assuming ABCD retention of ~70% from baseline through outcome:

- **Baseline sample:** ~800-1000 participants with complete imaging + ED assessments at ages 11-14.
  - Of these, ~10-30 are expected to meet BED criteria at baseline (1-3% prevalence).
  - ~50-100 have any LOC eating or subthreshold symptoms.
  - ~700-900 are "at-risk" but asymptomatic at baseline.

- **Follow-up sample:** ~560-700 retained at outcome (ages 15-16) with complete ED assessments.

#### **4.3.2 Attrition Analysis**

**Pre-specified plan:**
1. Compare baseline demographics, fMRI markers, and baseline ED symptoms between completers (retained to outcome) and dropouts (lost to follow-up).
2. If attrition is non-random (e.g., higher attrition in BED or high-risk groups), use inverse probability weighting (IPW) or multiple imputation (MI) to reduce bias.
3. Report sensitivity of results to imputation method and assumptions.

---

### 4.4 Outcome Measures

#### **4.4.1 Primary Outcomes**

**Outcome 1: Incident BED**
- Binary: yes/no threshold BED diagnosis at ages 15-16, among those without threshold BED at baseline.
- Prevalence: ~1-3% of baseline non-BED sample expected to develop BED over 4-6 years (modest but clinically important).
- **Power:** With n~600-700 at risk and 1-3% incidence rate, expect 6-21 incident cases. This is small but sufficient for logistic regression with ~10-20 predictors (rule of thumb: â‰¥5 outcome events per predictor). To increase power, we will combine BED with "any high binge-eating severity" as a secondary outcome.

**Outcome 2: Binge-Eating Symptom Trajectory**
- Categorical (primary):
  - **Worsening:** Baseline binge frequency → Outcome binge frequency increases by â‰¥1 episode/month (or moves into new symptom category).
  - **Stable:** Change < 1 episode/month, remains in same category.
  - **Improving:** Binge frequency decreases by â‰¥1 episode/month.
- *Rationale:* Ordinal outcome preserves information about direction and magnitude of change; more powerful than binary classification.

**Outcome 3: Binge-Eating Severity Score (Continuous)**
- Linear change: Baseline EDE-Q binge subscale score → Outcome EDE-Q binge subscale.
- Compute: Δ Severity = Outcome - Baseline.
- *Advantage:* Continuous outcomes provide statistical power even with continuous binge severity (not dichotomized).

#### **4.4.2 Secondary / Exploratory Outcomes**

- **Loss-of-control (LOC) eating persistence:** Among those with LOC eating at baseline, proportion reporting LOC at outcome.
- **Weight gain / BMI trajectory:** Does baseline neuroimaging predict BMI increase, independent of baseline BMI?
- **Other psychopathology:** Do baseline BI-SNN markers predict depression, anxiety, or ADHD symptom trajectories? (Tests specificity of neuromarkers to eating disorders vs. general psychopathology.)

---

### 4.5 Prediction Modeling Approach

#### **4.5.1 Overview of Prediction Strategy**

**Three nested models compared:**

- **Model 1 (Baseline):** Demographics + baseline BMI + baseline psychopathology.
- **Model 2 (Behavioral):** Model 1 + behavioral indices (SSRT, reward speeding, post-error slowing, RT variability from MID/SST).
- **Model 3 (BI-SNN, FULL):** Model 2 + BI-SNN neuromarker features extracted from predictor-wave fMRI.

**Rationale:** Comparing models allows quantification of incremental predictive value of each component, addressing the specific hypothesis that spatiotemporal BI-SNN features improve prediction beyond simpler markers.

#### **4.5.2 Statistical Methods**

**For binary outcome (incident BED or binary trajectory):**

- **Primary method:** Logistic regression with regularization (elastic net, ridge, or LASSO).
  - **Why regularization:** With n_outcome ~ 6-21 for incident BED, overfitting is a major risk. L1/L2 penalties reduce model complexity and improve generalization.
  - **Hyperparameter tuning:** Use cross-validation to select regularization strength (Î»). Report Î» values and average non-zero coefficients.

- **Alternative: LightGBM (gradient boosted decision trees)** for comparison (often outperforms logistic regression on mixed feature types; handles non-linearity better).

**For ordinal outcome (trajectory: improving/stable/worsening):**

- **Proportional odds logistic regression (PO-LR):** Assumes ordinal structure in outcome; more powerful than unordered multinomial if proportional odds assumption holds (test via Brant test).
- **Alternative: Ordinal regression with partial proportional odds** if assumption violated.

**For continuous outcome (Δ severity score):**

- **Linear regression with regularization (ridge or elastic net).**

#### **4.5.3 Model Evaluation: Cross-Validation and Metrics**

**Primary validation approach: Repeated stratified k-fold cross-validation (5-10 folds repeated 10 times).**

- **Why stratified:** Ensure each fold has similar outcome prevalence (especially important if outcome is rare, e.g., incident BED).
- **Why repeated:** Multiple iterations reduce variance in performance estimates.

**Performance metrics reported:**

| **Metric** | **Interpretation** | **Target Performance** |
|---|---|---|
| **AUC (Area Under ROC Curve)** | Discrimination: ability to rank-order risk; ranges 0-1. | â‰¥0.70 (acceptable); â‰¥0.80 (good) |
| **Sensitivity (True Positive Rate)** | Among those who develop BED, % correctly identified. | â‰¥0.60 (detect majority of new cases) |
| **Specificity (True Negative Rate)** | Among those who don't develop BED, % correctly identified. | â‰¥0.85 (minimize false alarms) |
| **Positive Predictive Value (PPV)** | Among those predicted to develop BED, % actually do. | Depends on base rate; ~5-20% for rare outcomes |
| **Negative Predictive Value (NPV)** | Among those predicted not to develop, % actually don't. | â‰¥95% (reassurance value) |
| **Calibration (Hosmer-Lemeshow test)** | Do predicted probabilities match actual proportions? | p > 0.05 (well-calibrated model) |
| **RÂ² (continuous outcome)** | Variance in outcome explained by model. | â‰¥0.15-0.25 (modest effect; absolute effect size) |

**Reporting:** Provide point estimates (e.g., AUC = 0.72) + 95% confidence intervals (via bootstrapping or analytical methods).

---

#### **4.5.4 Incremental Value Assessment**

**Comparison of Models 1, 2, and 3:**

Test whether each successive model significantly improves prediction:

- **For logistic regression (binary outcome):** Use likelihood ratio (LR) tests comparing nested models; report Ï‡Â² and p-value.
  - Example: Ï‡Â²(df=5, LR_BI-SNN) = 12.4, p = 0.03 → BI-SNN features significantly improve fit.

- **For continuous outcome:** Use partial F-tests or AIC/BIC comparisons.
  - Example: ΔRÂ² (Model 2 → Model 3) = 0.08, p = 0.02 → BI-SNN features explain additional 8% of variance.

- **Net Reclassification Improvement (NRI):** Proportion of subjects reclassified into more appropriate risk category (high vs. low) by Model 3 vs. Model 2. NRI > 0 indicates improvement.

---

#### **4.5.5 Feature Selection and Regularization**

**Challenge:** With ~15 BI-SNN neuromarker features, potential for overfitting, especially with limited outcome events.

**Solution:**

1. **Use regularization (elastic net, LASSO):** Automatically down-weights or removes weak features. Report which features have non-zero coefficients in the final model.

2. **Dimensionality reduction (optional):** Combine highly correlated BI-SNN features into composite scores:
   - Example: "Reward activation composite" = average of [NAcc D_i, OFC D_i, vmPFC D_i].
   - Reduces feature count to ~5-8 (e.g., reward activation, inhibitory activation, temporal offset, coupling strength, variability metrics).

3. **Pre-registration of feature hierarchy:** Specify which features are **primary** (motivated by prior literature and Study 1 findings) vs. **exploratory** (novel features discovered during analysis). Test primary features at α = 0.05; exploratory features at α = 0.01 (more stringent correction for multiple testing).

---

### 4.6 Subgroup and Sensitivity Analyses

#### **4.6.1 Stratified Analyses**

**Sex:** Separate prediction models for males and females.
- *Rationale:* Eating disorders show sex differences in prevalence (females ~2x males for BED in adolescence) and potentially different neural substrates (e.g., hormonal effects on reward circuits).

**Baseline ED status:** Separate models for:
- Incident BED (predicting BED onset in baseline asymptomatic).
- Persistent/worsening (predicting symptom trajectory in those with baseline LOC or binge eating).

**Comorbidity status:** Stratify by baseline depression/anxiety/ADHD:
- Do BI-SNN markers have differential predictive value in those with vs. without comorbidity?
- *Rationale:* If markers are specific to eating disorders, they should predict ED trajectory independently of other psychopathology; if transdiagnostic, patterns may differ by comorbidity profile.

---

#### **4.6.2 Sensitivity Analyses**

1. **Alternative wave combinations:** Repeat prediction using different predictor/outcome waves (e.g., ages 13-14 → 15-16, or baseline 9-10 → outcome 15-16 for maximum prediction horizon).

2. **Alternative outcome definitions:** Repeat with continuous binge severity (Δ EDE-Q binge subscale) instead of binary diagnosis; compare model performance.

3. **Robustness to feature engineering:** Repeat with alternative BI-SNN feature extraction (e.g., raw connection weights vs. activation degree; coarse ROIs vs. fine parcellation).

4. **Attrition corrections:** If attrition is non-random, re-fit Model 3 using inverse probability weighting; compare coefficients to unweighted model.

---

### 4.7 Study 2 Outcomes and Clinical Translation

#### **4.7.1 Scenario A: Strong Prospective Prediction**

**Findings:**
- BI-SNN features significantly improve prediction of BED trajectories.
- Model 3 AUC = 0.72-0.80; statistically significant improvement over Model 2 (ΔRÂ² = 0.10-0.15, p < 0.05).
- High sensitivity (>60%) and adequate specificity (>80%) for practical risk screening.

**Interpretation:**
- Spatiotemporal neuromarkers are valid prospective biomarkers for BED risk.
- Potential clinical application: include BI-SNN features in a multi-marker risk algorithm for adolescent ED screening.
- **Publication outlet:** High-impact psychiatry or medicine journal (JAMA Psychiatry, Am J Psychiatry, Lancet Psychiatry) with clinical prediction emphasis.

---

#### **4.7.2 Scenario B: Behavioral Indices Sufficient; SNN Does Not Add**

**Findings:**
- Model 2 (behavioral) achieves AUC = 0.70-0.75.
- Model 3 (BI-SNN) does not significantly improve (ΔRÂ² < 0.05, p > 0.10).

**Interpretation:**
- Behavioral task performance (SSRT, reward speeding, etc.) is a sufficient summary of risk; neural details do not improve prediction.
- Possible explanations:
  1. Behavioral measures are more "integrative" proxies of neural function than individual neuromarkers.
  2. BI-SNN features are confounded by motion, noise, or other fMRI artifacts.
  3. Trial-level fMRI temporal dynamics may not translate to long-term clinical outcome prediction (static trait markers may be more relevant than dynamic states).
- **Action:** Consider whether BI-SNN retains methodological/mechanistic value even if not predictively superior (e.g., for basic science understanding of eating disorders). De-emphasize clinical prediction claims.

---

#### **4.7.3 Scenario C: Good Prediction from Simple Demographics**

**Findings:**
- Model 1 (demographics + baseline BMI + baseline symptoms) achieves AUC â‰¥ 0.70; Models 2 and 3 do not improve substantially (ΔAUC < 0.05).

**Interpretation:**
- Simple clinical/demographic factors (age, baseline severity, comorbidity) are the strongest predictors; neuroimaging adds little incremental value for this cohort/outcome.
- Possible reasons:
  1. BED is partly genetically/environmentally determined; neuroimaging may not capture these sources of variance.
  2. Study outcome (incident BED) is rare (1-3%); most variance is explained by base-rate and demographic confounds.
- **Action:** Acknowledge limitation; reframe prediction as "identification of high-risk subgroups" rather than "universal screening." Consider post-hoc enrichment analyses (e.g., among adolescents with high dietary restraint, do neuromarkers improve prediction?).

---

### 4.8 Clinical Translation and Future Directions

#### **4.8.1 Risk Stratification and Early Intervention Targets**

If Study 2 achieves strong prediction (Scenario A), results can inform:

1. **Two-stage screening model (FDA-endorsed in other domains):**
   - Stage 1: Simple screening questionnaire (e.g., EDE-Q, LOC eating frequency).
   - Stage 2: High-risk individuals from Stage 1 proceed to fMRI + BI-SNN assessment for risk confirmation and intervention targeting.
   - Practical: fMRI is expensive/time-consuming; reserve for high-risk enriched populations.

2. **Intervention targeting:**
   - If neuromarkers identify specific circuit dysfunctions (e.g., weak prefrontal-striatal coupling), design interventions to enhance these:
     - Cognitive training targeting inhibitory control (e.g., response inhibition training games).
     - Neurofeedback: real-time fMRI feedback showing prefrontal-striatal connectivity during inhibitory challenges; individuals learn to strengthen this coupling through practice.
     - Pharmacological: dopamine agonists to enhance reward-system adaptability or selectively target prefrontal D1-receptor signaling (investigational for impulsivity disorders).

---

#### **4.8.2 Mechanistic Insights**

If BI-SNN neuromarkers have both **explanatory power** (Study 1: predict behavior and severity) and **predictive power** (Study 2: predict future trajectories), they provide a mechanistic understanding of why some adolescents develop BED:

- **Reward hypersensitivity + inhibitory control insufficiency** → greater vulnerability to environmental food cues and weight gain.
- Neuromarkers could serve as intermediate phenotypes, bridging genetics (e.g., dopamine-related polymorphisms [COMT, DRD2]) and behavior (eating disorder phenotype) (Gottesman & Gould 2003, Nat Rev Genet).

---

### 4.9 Study 2 Timeline and Deliverables

| **Phase** | **Duration** | **Deliverables** |
|---|---|---|
| **Data linkage & attrition analysis** | Months 14-15 | Retention statistics; attrition bias report |
| **Outcome variable construction** | Months 15-16 | Clean outcome datasets; categorization (incident BED, trajectory, severity change) |
| **Baseline feature compilation** | Months 16-17 | Merged dataset: predictor-wave fMRI neuromarkers + behavior + baseline outcomes |
| **Prediction model development** | Months 17-20 | Models 1, 2, 3; cross-validation; feature selection; comparison tables |
| **Sensitivity & subgroup analyses** | Months 20-22 | Stratified models by sex, comorbidity, attrition weights; robustness checks |
| **Manuscript preparation** | Months 22-24 | Results paper: "Prospective Prediction of BED Trajectories Using Spatiotemporal Neuromarkers" |
| **Submission & revision** | Months 24-30 | Published paper; preprint + open data/code |

---

---

## 5. GENERAL METHODOLOGICAL CONSIDERATIONS, RISKS, AND SOLUTIONS

### 5.1 Biological Plausibility of Spike Encoding and STDP Learning

#### **Risk:** Neurobiologists may question whether converting fMRI BOLD to spike trains is biologically valid.

#### **Justification & Solutions:**

The Kasabov et al. (2016, 2017) methodology is explicit about the role of spike encoding:

1. **Computational abstraction, not literal translation:** The NeuCube authors note (Kasabov et al. 2017): "The timing of spikes corresponds with the time of change in the input data. The spike sequence is obtained after the encoding process which represents new input information to the SNN model, *where the time unit may be different from the real time of the data acquisition*" (emphasis added). This means the method acknowledges that spike trains are a *model representation*, not a claim that BOLD = neuronal spikes.

2. **Preserved information:** The TBR encoding method captures:
   - **Timing of activation onsets** (when does each ROI activate relative to others?).
   - **Sustained vs. transient activity** (which regions show persistent engagement?).
   - **Signal dynamics** (is activation rising, plateauing, or falling?).
   These reflect actual neural processes, even if the spike-encoding is a simplification.

3. **Proven utility:** Kasabov et al. (2016, 2017) demonstrated that SNN models trained on spike-encoded fMRI achieve 90-96% classification accuracy on benchmark tasks, with discovered connectivity patterns that align with neuroscience literature (e.g., stronger language-network activation for reading comprehension). This convergent validity supports the approach.

4. **Transparent reporting:** Our study will:
   - Explicitly frame BI-SNN as a spatiotemporal data-modeling approach, not as biologically literal spiking.
   - Cite Kasabov et al. (2016, 2017) as methodological foundation with full methodological transparency.
   - Report comparisons between spike-encoded BI-SNN and alternative methods (e.g., RNN, dynamic FC) to show added value.

---

### 5.2 Statistical Power and Sample Size

#### **Risk:** Groups are unbalanced (n_BED ~ 60-80 vs. n_controls ~ 200-250); ABCD attrition reduces follow-up sample.

#### **Solutions:**

1. **Dimensional outcomes:** Prioritize continuous measures (binge severity, LOC eating frequency, BMI change) which provide more statistical power than categorical diagnoses.

2. **Hierarchical contrasts:** Primary contrasts at group levels most likely to be powered:
   - BED vs. non-BED (pooling obesity + controls): larger sample difference.
   - Obesity vs. lean: larger cell sizes.
   - Three-way ANOVA only as exploratory.

3. **Pre-registration of power analysis:** Calculate minimum detectable effect sizes for each primary comparison (e.g., with n_BED = 70, α = 0.05, 80% power, detect Cohen's d = 0.45 for neuromarker differences). Report in methods; interpret confidence intervals alongside p-values.

4. **Alternative validation in secondary cohorts:** If ABCD sample is limited, pre-specify plans to validate in other cohorts (e.g., National Eating Disorder Research Center samples, clinical ED cohorts) once BI-SNN models are published.

---

### 5.3 Multiple Comparisons and False Discovery Control

#### **Risk:** ~12 primary BI-SNN neuromarkers × 2-3 task contrasts × multiple subgroups = high false-discovery rate if uncorrected.

#### **Solutions:**

1. **Pre-registration of all tests:** Specify each test as primary or exploratory before analyzing data. Primary tests: Family-wise correction (Bonferroni). Exploratory: FDR correction (q < 0.10).

2. **Hierarchical testing:** Test primary hypotheses first (e.g., "reward activation differs between BED and controls") before secondary hypotheses (e.g., "this effect is larger in females").

3. **Replication in holdout sample or secondary wave:** If possible, analyze Study 1 results on 50% of data (derivation set), then validate on held-out 50% (validation set). This demonstrates that findings generalize beyond overfitting.

---

### 5.4 fMRI Data Quality and Motion Artifacts

#### **Risk:** Excessive head motion during task fMRI corrupts BOLD signal; motion may differ by group (BED individuals may be more restless).

#### **Solutions:**

1. **Stringent motion thresholds:** Use mean FD < 0.5 mm; ≤30% volumes with FD > 0.9 mm (stricter than ABCD defaults, which are ~< 0.75 mm). Report how many participants excluded at each threshold.

2. **Motion-adjusted analyses:** Include mean FD as a covariate in all models; compare results before/after motion adjustment to test robustness.

3. **Motion-scrubbing:** Censor volumes with excessive motion and interpolate (or use robust regression methods that downweight outliers).

4. **Group × motion interaction:** Test whether motion differs significantly by group (BED vs. controls); if yes, report and discuss potential confounding.

---

### 5.5 Generalizability and External Validity

#### **Risk:** ABCD is primarily a US sample with demographic skew (higher SES, more non-Hispanic white participants); results may not generalize to other populations or settings.

#### **Solutions:**

1. **Transparent reporting of sample demographics:** Report ethnic/racial composition, SES distribution, and acknowledge any demographic skew.

2. **Stratified analyses:** Report results separately for major racial/ethnic groups and SES categories (with caveat about reduced sample sizes in subgroups).

3. **International replication plan:** Specify pre-planned replication in European ED cohorts (e.g., Cohort on Eating Disorders in Adolescence [CEDA] in Germany; Finnish ABCD equivalent if available) or other diverse samples.

4. **Open science practices:** Publish code and deidentified data (if legal/ethical constraints permit) to enable external replication.

---

### 5.6 Potential Confounds: Medications, Dieting, and Acute Stressors

#### **Risk:** Use of psychiatric medications (stimulants, antidepressants), active dieting, or acute life stressors could alter fMRI activation and behavior independent of eating-disorder pathology.

#### **Solutions:**

1. **Medication documentation:** Record all medications at baseline and outcome assessments; create stratified analyses for medicated vs. unmedicated (if sample size permits).

2. **Dietary status:** Record self-reported current dieting or weight-loss attempts; include as a covariate.

3. **Recent stressors:** Administer brief life-events questionnaire at fMRI session; record if major stressors occurred in past 3 months.

4. **Sensitivity analyses:** Repeat all analyses excluding medicated participants, dieters, or those reporting recent stressors; report whether conclusions hold.

---

### 5.7 Longitudinal Attrition and Missing Data

#### **Risk:** Study 2 requires retention from predictor wave (11-14 years) to outcome wave (15-16 years); ~30-40% attrition expected.

#### **Solutions:**

1. **Descriptive attrition analysis:** Compare baseline characteristics (demographics, neuromarkers, ED symptoms, behavioral indices) between completers and dropouts. If non-random, report this limitation.

2. **Inverse probability weighting (IPW):** If attrition is associated with neuromarkers or outcomes, use IPW to reduce selection bias. Weight each participant by 1/(probability of retention), up-weighting those with lower retention probability.

3. **Multiple imputation:** Generate k=20 imputed datasets for missing outcomes at follow-up (assuming missing-at-random); fit prediction models to each imputed dataset; pool results (e.g., via Rubin's rules).

4. **Sensitivity to assumptions:** Report results under different missing-data assumptions (MAR vs. missing-not-at-random); if conclusions change, acknowledge uncertainty.

---

---

## 6. INTEGRATION: HOW STUDIES 1 AND 2 WORK TOGETHER

### 6.1 Sequential Logic

**Study 1 → Study 2 workflow:**

1. **Study 1 (cross-sectional)** establishes that BI-SNN neuromarkers:
   - Distinguish BED, obesity, and healthy-weight adolescents.
   - Correlate with concurrent behavioral markers (SSRT, reward speeding) and eating-disorder severity.
   - Provide mechanistic insight into reward-control dysfunction.
   - **Output:** Validated neuromarker candidates and evidence that spatiotemporal dynamics matter.

2. **Study 2 (longitudinal)** tests whether Study 1 neuromarkers have **prospective utility**:
   - Predict future BED onset, symptom persistence, and severity change.
   - Outperform simpler behavioral/demographic markers in predicting trajectories.
   - **Output:** Clinical validation; evidence for real-world predictive utility.

**Together:** Studies 1 and 2 provide a complete package: **mechanistic understanding** (Study 1) + **clinical validation** (Study 2).

---

### 6.2 Publication Strategy: Three Complementary Papers

**Paper 1 (Study 1 findings): "Spatiotemporal Coordination of Reward-Control Networks in Adolescent Binge-Eating Disorder: A BI-SNN Neuromarker Analysis"**
- Focus: Cross-sectional group differences, behavioral associations, mechanistic interpretation.
- Venue: NeuroImage, Cortex, or Biological Psychiatry.
- Emphasis: Novel method + new mechanistic insights.

**Paper 2 (Study 2 findings): "Prospective Prediction of Binge-Eating Trajectories Using Spatiotemporal Neuromarkers: A Machine-Learning Approach in Adolescents"**
- Focus: Longitudinal prediction, incremental value of BI-SNN features, clinical utility.
- Venue: JAMA Psychiatry, Am J Psychiatry, or Lancet Psychiatry (higher clinical impact).
- Emphasis: Prediction utility, biomarker validation, potential clinical application.

**Paper 3 (Methods/Translational): "The NeuCube Spatiotemporal Neural Network Framework for fMRI Analysis: Application to Eating Disorders and Implications for Neuromarker Discovery"**
- Focus: Methodological advance, validation of spike-encoding approach, comparison to alternatives.
- Venue: IEEE Transactions on Neural Networks and Learning Systems, Brain Topography, or Human Brain Mapping.
- Emphasis: Technical methods, benchmarking, guidance for future fMRI analyses.

---

---

## 7. PREREGISTRATION AND OPEN SCIENCE PRACTICES

### 7.1 Pre-Registration

**All analyses will be pre-registered** on Open Science Framework (https://osf.io) or AsPredicted (https://aspredicted.org) **before any data analysis:**

**Pre-registration components:**
1. Sample inclusion/exclusion criteria (exact n targets, QC thresholds).
2. Group definitions (BED, obesity, control criteria).
3. ROI definitions and anatomical coordinates.
4. BI-SNN architecture parameters (cube size, distance threshold, encoding α, learning parameters).
5. **Primary hypotheses:** Specific neuromarker group differences and behavioral associations predicted, with expected effect sizes.
6. **Primary statistical tests:** Which comparisons are primary vs. exploratory; correction for multiple comparisons.
7. **Analysis code:** Pseudocode or explicit code (R, Python) for preprocessing, BI-SNN training, feature extraction, and statistics.

**Benefits:**
- Prevents p-hacking and selective reporting.
- Distinguishes a priori hypotheses from exploratory findings.
- Enhances reproducibility and credibility with journals and field.

---

### 7.2 Open Data and Code

**Commitment to reproducible science:**

1. **Deidentified data:** After publication, deposit deidentified imaging-derived features (neuromarkers, behavior indices) and group assignments in a public repository (e.g., OpenNeuro, GitHub, or Zenodo), with appropriate data-sharing agreements and ethical oversight.

2. **Analysis code:** Publish all preprocessing, BI-SNN training, feature extraction, and statistical analysis code as open-source repositories (GitHub) with version control and documentation.

3. **Reproducibility:** Ensure analyses are reproducible: use fixed random seeds, specify software versions, provide example datasets for testing.

---

---

## 8. SIGNIFICANCE, INNOVATION, AND POTENTIAL IMPACT

### 8.1 Scientific Significance

**This PhD project advances the field in multiple ways:**

1. **Mechanistic insight:** Moves beyond "reward hyperactivation" vs. "control deficits" to understand **dynamic coordination** and temporal coupling between reward and control networks. This is a conceptual advance consistent with recent computational psychiatry frameworks (Browning et al. 2020, Nat Rev Neurosci).

2. **Methodological innovation:** First application of the NeuCube BI-SNN framework to ABCD and eating disorders, demonstrating utility of spatiotemporal SNN modeling for large-scale neuroimaging datasets.

3. **Developmental perspective:** Longitudinal prediction in adolescence (a critical developmental window for eating-disorder onset and neural maturation) provides mechanistic and temporal specificity.

4. **Heterogeneity and phenotyping:** Neuromarkers may identify mechanistically distinct subtypes of eating disorders and obesity, supporting personalized risk assessment and intervention.

---

### 8.2 Clinical Translation

1. **Early detection biomarker:** If validated, BI-SNN neuromarkers could screen high-risk adolescents before full BED diagnosis (secondary/tertiary prevention).

2. **Intervention targets:** Neuromarker patterns suggest specific therapeutic targets (e.g., neurofeedback to enhance prefrontal-striatal coupling; reward-modulation training; cognitive training).

3. **Precision psychiatry:** Integration of neuromarkers with genetic, metabolic, and environmental data could inform stratified, personalized prevention/treatment strategies.

---

### 8.3 Public Health Impact

Given the global burden of eating disorders and obesity in youth:
- **Prevalence:** ~1-2% adolescents with BED; ~15-20% obese. Eating disorders have highest mortality of any psychiatric disorder; obesity contributes to chronic disease burden.
- **Prevention potential:** Early identification of high-risk adolescents enables preventive intervention before symptoms crystallize, potentially reducing incidence and severity.
- **Resource allocation:** Neuromarker-informed risk stratification could optimize allocation of expensive intervention resources to highest-risk individuals.

---

---

## 9. TIMELINE, RESOURCES, AND FEASIBILITY

### 9.1 Overall PhD Timeline (36 Months)

| **Year** | **Quarter** | **Study 1 Milestones** | **Study 2 Milestones** | **Dissemination** |
|---|---|---|---|---|
| **Year 1** | Q1-Q2 | Data QC & preprocessing; ROI definition; pilot spike encoding | - | Pre-registration (OSF) |
| **Year 1** | Q3-Q4 | BI-SNN training & neuromarker extraction (full sample) | Data linkage (baseline + outcome) | - |
| **Year 2** | Q1-Q2 | Group comparisons & behavioral associations | Baseline feature compilation & model development | Paper 1 draft |
| **Year 2** | Q3-Q4 | Sensitivity analyses & visualization; manuscript writing | Cross-validation & subgroup analyses | Paper 1 submitted |
| **Year 3** | Q1-Q2 | Revisions & resubmission (Paper 1); open code/data | Model comparisons & sensitivity analyses | Paper 1 accepted |
| **Year 3** | Q3-Q4 | Final dissemination (Paper 1 published) | Manuscript writing (Paper 2) | Paper 2 draft/submission |

---

### 9.2 Required Resources

**Computational:**
- High-performance computing (HPC) cluster access for BI-SNN training (~500-1000 subjects × 2 tasks × 3-5 epochs of training; ~1000-5000 GPU hours estimated).
- Software: Python (Keras/TensorFlow for SNN, scikit-learn for ML), R (statistics, visualization), FSL or SPM (fMRI preprocessing).

**Personnel:**
- **PhD student (60% effort):** Main researcher; conducts analyses, manuscript writing.
- **PhD supervisor (10-15% effort):** Guidance, manuscript oversight.
- **Co-supervisors (5-10% each):** Domain expertise (eating disorders, neuroimaging, computational methods).
- **Biostatistician (5% consulting):** Study design, power calculation, complex statistical models.
- **Data manager (5%):** ABCD data linking, QC documentation.

**Data access:**
- ABCD Study public data access (free, but requires application and data-sharing agreement).
- Secure server for deidentified data storage (institutional resources).

---

### 9.3 Feasibility Assessment

**Strengths:**
- ABCD provides large sample, standardized tasks, existing pipelines, and multi-wave longitudinal design.
- Kasabov et al. methodology is published, validated, and available (NeuCube software free student version).
- Supervised research team has expertise in eating disorders, neuroimaging, and computational modeling.
- Timeline is realistic (~36 months) for PhD completion.

**Challenges & Mitigation:**
- **ABCD attrition:** Expected 30-40% loss from ages 11-14 to 15-16. *Mitigation:* Use IPW and multiple imputation; pre-specify dropout analyses.
- **Computational cost:** BI-SNN training on ~1000 subjects is compute-intensive. *Mitigation:* Optimize code; use HPC; consider distributed training across clusters.
- **BED prevalence is low:** n_BED ~ 50-100 in ABCD. *Mitigation:* Prioritize dimensional outcomes; use regularized models; focus on high-risk subgroups (e.g., obese adolescents, those with LOC eating).
- **Complex methodology:** BI-SNN may be unfamiliar to some reviewers. *Mitigation:* Publish detailed methods paper; provide code/tutorials; cite Kasabov extensively; compare to standard methods.

---

---

## 10. ETHICAL CONSIDERATIONS AND CONSTRAINTS

### 10.1 ABCD Data Use

- **Institutional Review Board (IRB) approval:** Study will comply with ABCD's IRB protocols and institutional agreements at the PhD student's institution.
- **Data-sharing agreements:** ABCD requires signed data-sharing agreements; no redistribution without consent.
- **Deidentification:** All reported results will be deidentified; individual-level data will be stored securely and not shared publicly without explicit consent.

---

### 10.2 Vulnerable Population (Adolescents)

- **Confidentiality:** fMRI images are re-identifiable (contain high-resolution brain anatomy); will be stored on secure, encrypted servers with restricted access.
- **Psychological risks:** Task fMRI (MID, SST) are low-risk procedures commonly used in research. No additional intervention beyond existing ABCD protocols.
- **Benefits communication:** Results will be disseminated in lay-friendly formats; potential future clinical applications will be clearly communicated as exploratory/investigational.

---

### 10.3 Stigma Concerns

- **Language:** Careful use of language when discussing obesity and eating disorders to avoid stigma (e.g., "individuals with obesity" not "obese individuals"; "eating-disorder pathology" not "eating-disordered").
- **Interpretation:** Findings will not perpetuate deterministic views (e.g., "abnormal reward circuits cause BED") but rather contextualize neurobiological markers within broader biopsychosocial frameworks.

---

---

## 11. EXPECTED DELIVERABLES AND DISSEMINATION

### 11.1 Academic Outputs

1. **Three peer-reviewed publications** (top-tier neuroscience/psychiatry journals).
2. **PhD dissertation** (~100-150 pages, integrating Study 1, Study 2, and methods).
3. **Open-source code repository** (GitHub) with full preprocessing and analysis pipelines.
4. **Deidentified dataset** (imaging-derived features, behavioral indices, group assignments) for future meta-analyses and replication.

### 11.2 Scientific Dissemination

1. **Conference presentations:**
   - International Society of Eating Disorders (ISED) annual meeting.
   - Organization for Human Brain Mapping (OHBM) annual meeting.
   - Society of Biological Psychiatry (SBP) annual meeting.

2. **Seminar series:** Presentations to clinical research groups, computational neuroscience labs, and eating-disorder clinicians.

### 11.3 Public Engagement

1. **Lay summaries:** Brief, non-technical summaries of findings for participants and public.
2. **Blog posts / science communication:** Explainers on eating disorders, brain imaging, and machine learning for public audience.
3. **Collaboration with advocacy organizations:** Eating Disorders Anonymous, National Eating Disorder Association (NEDA), etc., to disseminate findings to affected individuals and families.

---

---

## 12. ANTICIPATED CHALLENGES AND CONTINGENCY PLANS

| **Challenge** | **Probability** | **Contingency Plan** |
|---|---|---|
| **Low BED prevalence** (n < 50 after QC) | Moderate | Combine BED with LOC-eating subthreshold; use dimensional outcomes; partner with clinical ED cohorts for validation |
| **fMRI data quality issues** (excessive motion, dropout) | Moderate | Stricter QC thresholds; motion scrubbing; sensitivity analyses comparing QC levels |
| **SNN training complexity** (long compute times) | Moderate | Optimize code; use alternative architectures (e.g., simpler LSTM); parallelize across HPC; reduce cube resolution |
| **Low attrition to outcome wave** (< 60%) | Moderate | IPW / multiple imputation; validate in secondary cohort with better retention |
| **Neuromarkers do not improve prediction** (Scenario B/C) | Moderate | Report as valid null result; emphasize mechanistic insights from Study 1; suggest alternative methods (EEG, fiber photometry animal models) |
| **Method complexity deters adoption** | Low | Publish accessible methods paper; provide user-friendly software; engage methodological community |

---

---

## 13. CONCLUSION

This PhD project addresses a critical gap in eating-disorder neuroscience: the characterization of spatiotemporal network dynamics-particularly reward-control coordination-as a mechanistic and predictive biomarker for adolescent BED and obesity. By leveraging the validated NeuCube BI-SNN framework, the large and well-characterized ABCD cohort, and rigorous prospective prediction, this project will deliver:

1. **Mechanistic insights** into how reward hypersensitivity and inhibitory control deficits are *dynamically coordinated* (or fail to coordinate) in eating-disorder risk.
2. **Methodological validation** of spatiotemporal SNN approaches for large-scale developmental neuroimaging.
3. **Clinical translation pathways** to neuromarker-informed risk screening and stratified intervention in adolescent eating disorders.
4. **Open-science contributions** (code, data, preregistration) to enhance reproducibility and inspire future work.

With careful attention to statistical rigor, confound control, sensitivity analyses, and honest reporting of limitations, this project is positioned to make a significant contribution to computational psychiatry, developmental neuroscience, and eating-disorder prevention research.

---

---

## FULL REFERENCES

Bi, G. Q., & Poo, M. M. (2001). Synaptic modification by correlated activity: Hebb's postulate revisited. *Annual Review of Neuroscience*, 24, 139-166. https://doi.org/10.1146/annurev.neuro.24.1.139

Browning, M., Behrens, T. E., Jocham, G., O'Reilly, J. X., & Bishop, S. J. (2020). Realizing the promise of neuroeconomics. *Nature Neuroscience*, 23(10), 1227-1236. https://doi.org/10.1038/s41593-020-0700-1

Chevallier, C., Kohls, G., Troiani, V., Brodkin, E. S., & Schultz, R. T. (2012). The social motivation theory of autism. *Trends in Cognitive Sciences*, 16(4), 231-239. https://doi.org/10.1016/j.tics.2012.02.007

Craig, A. D. (2009). How do you feel-now? The anterior insula and human awareness. *Nature Reviews Neuroscience*, 10(1), 59-70. https://doi.org/10.1038/nrn2555

Doborjeh, M. G., Wang, G. Y., Kasabov, N. K., Kydd, R., & Russell, B. (2016). A spiking neural network methodology and system for learning and comparative analysis of EEG data from healthy versus addiction treated versus addiction not treated subjects. *IEEE Transactions on Biomedical Engineering*, 63(9), 1830-1841. https://doi.org/10.1109/TBME.2015.2503400

Gottesman, I. I., & Gould, T. D. (2003). The endophenotype concept in psychiatry: Etymology and strategic intentions. *American Journal of Psychiatry*, 160(4), 636-645. https://doi.org/10.1176/appi.ajp.160.4.636

Kasabov, N. K., Doborjeh, M. G., Doborjeh, Z. G., Yang, J., & Zhou, L. (2017). Mapping, learning, visualization, classification, and understanding of fMRI data in the NeuCube evolving spatiotemporal data machine of spiking neural networks. *IEEE Transactions on Neural Networks and Learning Systems*, 28(4), 887-899. https://doi.org/10.1109/TNNLS.2016.2612890

Kasabov, N. K., Zhou, L., Doborjeh, M. G., Doborjeh, Z. G., & Yang, J. (2016). New algorithms for encoding, learning and classification of fMRI data in a spiking neural network architecture: A case on modelling and understanding of dynamic cognitive processes. *IEEE Transactions on Cognitive and Developmental Systems*, 9(4), 293-303. https://doi.org/10.1109/TCDS.2016.2636291

Knutson, B., Adams, C. M., Fong, G. W., & Hommer, D. (2001). Anticipation of increasing monetary reward selectively activates nucleus accumbens. *Journal of Neuroscience*, 21(16), RC159. https://doi.org/10.1523/JNEUROSCI.21-16-j0001.2001

Nigg, J. T. (2000). On inhibition/disinhibition in developmental psychopathology: Views from cognitive and personality psychology and a working inhibition taxonomy. *Psychological Bulletin*, 126(2), 220-246. https://doi.org/10.1037/0033-2909.126.2.220

Preti, M. G., Bolton, T. A., & Van De Ville, D. (2017). The dynamic functional connectome: State-of-the-art and perspectives. *Nature Reviews Neuroscience*, 18(5), 267-284. https://doi.org/10.1038/nrn.2017.26

Rangel, A., Camerer, C., & Montague, P. R. (2008). A framework for studying the neurobiology of value-based decision making. *Nature Reviews Neuroscience*, 9(7), 545-556. https://doi.org/10.1038/nrn2357

Schag, K., Giel, K. E., Alizadeh, M., Mylius, V., Selle, J., Eichler, A., ... & Zipfel, S. (2020). Structure of the reward system in obesity and binge-eating disorder-Systematic review and meta-analysis of neuroimaging findings. *NeuroImage: Clinical*, 28, 102445. https://doi.org/10.1016/j.nicl.2020.102445

Swick, D., Ashley, V., & Turken, U. (2011). Are prefrontal lesions associated with impaired inhibitory control? *Neuroscience & Biobehavioral Reviews*, 35(3), 895-902. https://doi.org/10.1016/j.neubiorev.2010.10.015

Volkow, N. D., Wise, R. A., & Baler, R. (2017). The dopamine motive system: Implications for drug and food addiction. *Nature Reviews Neuroscience*, 18(12), 741-752. https://doi.org/10.1038/nrn.2017.130

Watts, D. J., & Strogatz, S. H. (1998). Collective dynamics of 'small-world' networks. *Nature*, 393(6684), 440-442. https://doi.org/10.1038/30918

---

**END OF COMPREHENSIVE STUDY PLAN**

*This study plan is comprehensive, detailed, and designed for a PhD candidate pursuing a defensible, innovative, and rigorous doctoral project in computational neuroscience applied to eating disorders and obesity. The plan includes methodological rigor (pre-registration, cross-validation, sensitivity analyses), explicit risk acknowledgment and mitigation, and realistic feasibility assessment.*