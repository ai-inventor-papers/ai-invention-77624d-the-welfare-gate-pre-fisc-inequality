# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `run_2nz_vV2E7aIl` — The Welfare Gate: Pre-Fisc Inequality, Universal Public Services, and Democratic Resilience in Post-1990 Democratizers
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_plan_dataset_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-09-05 11:36:26 UTC

````
<hypothesis>
kind: hypothesis
title: Welfare shields young democracies from inequality
hypothesis: |-
  STATEMENT: Among post-1990 democratizers whose transition began by 1998, a rise in market-income inequality (the WID pre-tax top-10% income share as the primary treatment, the market-income Gini as secondary) erodes liberal-democratic quality three to five years later only where welfare institutions built in the first democratic decade are thin. In countries whose first democratic decade universalized public health and education into services the broad middle class actually uses, market-inequality surges do not transmit into declines in the V-Dem Liberal Democracy Index; in countries where public services stayed thin, the same surges predict graded erosion. The gate is the universal service state, not welfare effort in general: total social spending (pension-heavy, targeted cash, chauvinist transfers) does not gate, and welfare generosity purchased later by incumbents is part of the erosion playbook, not a substitute.

  MEASUREMENT: THE TREATMENT MUST BE PRE-FISC. The disposable-income Gini is post-treatment with respect to automatic stabilization: high-welfare fiscal systems mechanically compress post-fisc inequality, so a gate interaction estimated on disposable Gini would load partly as definitional fiscal filtering even if no behavioral gate existed. The revised claim therefore separates the two paths the gate comprises: (i) automatic stabilization, measured directly as the market-minus-disposable Gini gap (the fiscal filter that absorbs part of any market shock before it reaches the distribution citizens experience); and (ii) behavioral transmission, the residual link from the market shock citizens do experience to democratic quality, gated by constituency formation via policy feedback (the middle class holds a material stake in the public institutions that erosion would capture; Pierson 1993; Soss and Schram 2007; microfoundation in Rothstein and Uslaner 2005) and by credible pre-commitment (automatic, entitlement-based universal programs pre-empt the elite-retrenchment and populist-promise equilibrium of Acemoglu, Egorov and Sonin 2013). Each mechanism has a discriminating implication: the market-minus-disposable gap (stabilization), the universal-versus-targeted composition of spending and middle-class usage (constituency formation), and program automaticity (pre-commitment). The polarization arm is retained only as a mechanism report, not as the gate's distinctive content, because Rau and Stokes already invoke inequality-induced polarization.

  IDENTIFICATION: THE GATE IS IDENTIFIED ON DEVIATIONS FROM WELFARE-SPECIFIC TRENDS. The core specification includes welfare (W) x time and W x time-squared interactions, because any factor correlated with both welfare depth and democratic trajectories (EU accession, fiscal capacity, geopolitical alignment) would otherwise masquerade as a gate. The gate claim survives only if the pre-fisc-inequality x W interaction remains significant once those trends, GDP level, region, and EU accession are controlled, with passing pre-trend tests in staggered event studies estimated with Callaway-Sant'Anna and Sun-Abraham estimators given differential treatment timing.

  THE PRE-DETERMINED WELFARE MEASURE. W = public health plus public education spending (percent of GDP, WHO and World Bank EdStats series on OWID), set to the earliest available three-year window within the first democratic decade (years 0-8 after transition), with the actual calendar window documented per country and the T+3..7 versus T+8..12 sensitivity pair reported so window drift is visible (WHO health series start near 2000, so actual measurement years are disclosed rather than assumed). The cohort cap (transition year at most 1998) ensures W precedes the 2008 crisis and the 2010-2022 resilience window for every retained case; early transitions whose de facto service data only begin around 2000 are kept but flagged. Countries with erosion onset within the first 12 years are excluded or recoded in robustness. W's exogeneity is probed directly: W regressed on first-decade inequality changes and fiscal-collapse indicators (inflation, output collapse); 2SLS with legacy instruments (communist-era schooling enrollment, colonial-era public-service coverage); and a within-Eastern-Europe estimate holding the communist legacy constant.

  THE WELFARE-DEPENDENT DIVIDEND. The inequality-reduction leg of the democratic dividend (Acemoglu, Naidu, Restrepo and Robinson 2015, stated on top-income shares, which is what that work actually reports, not on the Gini) materializes only in high-welfare-legacy countries, within the first post-transition years (dividend window years 0-7); the size of that first-decade dividend predicts 2010-2022 resilience. Where education expands without labor-market absorption (ILO educated-youth unemployment), the Campante-Chor mismatch tightens the gate only where welfare is thin.

  STATUS AND CRITERIA. No model has been estimated; this is a pre-registered, empirically untested hypothesis, not a finding. All estimation was postponed; the protocol, the fixed country roster with a coverage matrix (country x variable x window), and a simulation-based minimum-detectable-effect analysis (N of 25-35 retained countries under serial correlation rho 0.7-0.9) are to be deposited in a timestamped registry before estimation, with the effective estimation sample for each of the six designs pre-printed and listwise-deletion consequences below about 25 countries pre-specified. CONFIRMATION requires: (a) a significant positive pre-fisc-inequality x W interaction on liberal-democracy trajectories under welfare-specific trend controls, with the inequality marginal effect near zero or positive at high W and strongly negative at thin W, significant in the primary specification and in at least 5 of 7 pre-specified robustness cells, with failures reported and interpreted; (b) sequencing: market-inequality surges and public-service retrenchment lead Liberal Democracy Index declines by three to five years in thin-welfare countries only, no anticipatory service decline before erosion onset in the high-welfare arm, and pre-trend tests passing; (c) the welfare-dependent dividend: the top-10 percent share declines in years 0-7 after democratization only in high-welfare-legacy countries, and its size predicts 2010-2022 resilience; (d) at least one discriminating mechanism result, e.g., the gate attenuates once the market-minus-disposable gap is controlled (stabilization does part of the work), or the gate tightens with targeted or means-tested composition and discretionary transfers (constituency and pre-commitment); and (e) the universalism contrast with a full-sample transfer placebo (ILO World Social Protection Database or IMF GFS covering all retained countries), because the OECD-only SOCX subsample cannot carry the sharpest claim of the paper. DISCONFIRMATION: a homogeneous inequality effect across welfare arms; an insignificant or wrong-signed interaction; an interaction that collapses once W x time trends are added; reversed sequencing (erosion precedes service decline); a gate reproduced by the pension or targeted-cash placebo; or a dividend that appears in thin-welfare countries. Each outcome falsifies the hypothesis as stated and adjudicates among unconditional materialist, purely coalitional, and outcome-transformation accounts of post-1990 erosion; a null result is itself the contribution.

  MOTIVATION: The field holds two contradictory accounts of post-1990 erosion: the materialist (Rau and Stokes 2025 on uninterrupted democracies; Houle 2009 for the coup era) and the coalitional (Haggard and Kaufman 2021 from close case comparison). Neither tests the conditioning structure, and prior global tests were further entangled because disposable-income inequality is partly a product of the very welfare institutions hypothesized to gate. The welfare-gate hypothesis resolves the contradiction: inequality matters, but only where welfare institutions are too thin to absorb and convert it; both accounts hold in different institutional environments. Using market-income inequality as the treatment and measuring the fiscal filter directly makes the gate test and the test of the stabilization mechanism separable. For any future democratization wave the policy implication is unchanged and directly actionable: universal health and education systems must be built in the first democratic decade, before crises arrive. Everything remains testable on public OWID panels, with one disclosed non-OWID input, the Boix-Miller-Rosato cross-check for transition dating.

  ASSUMPTIONS: (1) The V-Dem Liberal Democracy Index (OWID) is a valid continuous measure of graded democratic quality for young democracies. (2) The WID pre-tax top-10 percent income share is a valid pre-fisc treatment orthogonal to fiscal filtering; the disposable-income Gini is robustness only. (3) Public health plus education spending at the earliest documented window within years 0-8 is a pre-determined proxy for universalistic services, not a product of first-decade inequality dynamics or fiscal collapse; probed by exogeneity regressions, 2SLS on legacy instruments, and recoding of early-erosion cases. (4) Post-1990 transitions (1989-1998) are quasi-exogenous in timing and welfare legacies (communist-era health and education systems, colonial-era public services) are inherited rather than chosen; every retained case has W measured before erosion onset and before the 2010-2022 resilience window. (5) No unobserved confounder drives both welfare maintenance and democratic resilience; this is probed by welfare-specific trend controls, within-Eastern-Europe analysis, placebo interactions (e.g., population age structure), and legacy-instrument 2SLS. (6) Cross-country comparability of PIP/WID inequality and WHO/EdStats spending series is adequate for the retained panel; coverage gaps (early-1990s PIP sparsity, WHO health from about 2000, ILO mismatch series availability, non-OECD transfer data) are documented in the coverage matrix and bound the effective estimation sample.

  INVESTIGATION APPROACH: OWID-only country-year panel, 1990-2022; treated sample of post-1990 democratizers with transitions 1989-1998 (about 25-35 countries), plus all democracies for comparison. Six pre-registered designs. Design 1 (gate test): two-way fixed-effects regression of the Liberal Democracy Index on lagged (t-3) pre-fisc inequality, its interaction with pre-determined W, country and year fixed effects, W x t and W x t-squared trends, GDP level, region, and EU-accession controls; marginal effects of inequality at the 10th, 25th, 50th, 75th and 90th percentiles of W with wild-cluster bootstrap; five-year-differences and Goodman-Bacon decomposition as checks. Design 2 (adjudication): baseline inequality main effect without interaction, then with interaction, on the full democracy sample and the young-democracy sample. Design 3 (sequencing): staggered erosion-onset event studies by welfare arm with Callaway-Sant'Anna and Sun-Abraham estimators and pre-trend tests, tracing inequality, public services, and the index around onset. Design 4 (democratization event study): dynamic path of the top-10 percent share and public services after transition by welfare legacy; dividend over years 0-7; first-decade dividend size predicting 2010-2022 index change. Design 5 (mechanisms): market-minus-disposable Gini gap as stabilizer measure; spending composition and middle-class usage proxies for constituency formation; program automaticity for pre-commitment; polarization and ILO educated-youth unemployment reported as mechanism arms. Design 6 (robustness): trend-controlled interaction, W exogeneity regressions and 2SLS on legacy instruments, exclusion of erosion-within-first-12-years cases, commodity-boom exclusion, population weights, alternative inequality and welfare measures, within-Eastern-Europe estimate, bootstrap confidence intervals, and the full-sample transfer placebo. Implemented in Python (linearmodels and statsmodels, clustered standard errors); zero external data beyond OWID plus the disclosed BMR/RoW transition cross-check; no LLM spend.

  RELATED WORK: Svolik 2015 (young democracies' distinct vulnerability to incumbent takeover defines the population at risk, but conditions nothing on institutions for the inequality channel, which the gate adds); Huber and Stephens 2001 and 2012 (welfare states underwrite democratic legitimacy and consolidation in Latin America: the closest existing statement of the gate's constituency logic, absent the inequality-shock interaction structure and the post-1990 cohort); Rothstein and Uslaner 2005 (universalism to equality to trust to institutional legitimacy: microfoundation for constituency formation); Rau and Stokes 2025 (unconditional materialist main effect, no moderators, sample excludes the post-1990 cohort, polarization already invoked there); Haggard and Kaufman 2021; Houle 2009; Acemoglu, Naidu, Restrepo and Robinson 2015 (dividend on taxation, schooling, and top-income shares, with imprecise Gini estimates, contrary to how the chapter is sometimes cited); Acemoglu, Egorov and Sonin 2013; Korpi and Palme 1998; Esping-Andersen 1990; Pierson 1993; Soss and Schram 2007; Szikra and Oektem 2023, Lendvai-Bainton and Szelewa 2021, Vanhuysse 2006, Benczes and Orzechowska-Waclawska 2024 (outcome side: welfare transformed under backsliding, separated from the gate by the lead-lag tests); Campante and Chor 2012 (absorption channel); Callaway and Sant'Anna 2021, Sun and Abraham 2021, Goodman-Bacon 2021 (staggered difference-in-differences).

  INSPIRATION: Three cross-domain transfers structure the hypothesis. (1) Control theory, disturbance rejection: the gain with which an exogenous disturbance propagates to a state variable depends on a feedback controller; the empirical translation is exactly the interaction design this literature has not run. (2) Public-health effect modification: institutions as modifiable protective exposures that gate a socioeconomic risk factor's harm, standard in epidemiology, almost absent from the inequality-democracy literature. (3) Ecology's resistance-versus-resilience distinction: fate of a disturbed system depends on buffering capacity, not the disturbance alone. The revision adds a fourth: the fiscal-filtering insight, in which the entanglement between post-fisc inequality and welfare institutions is turned into the direct, measured test of the stabilization mechanism, so the first mechanism is measured rather than assumed.

  TERMS: Liberal Democracy Index, post-1990 democratizers (now bounded to transitions 1989-1998), democratic erosion, welfare institutions, institutional gate (now conditioning the transmission of market-income shocks), democratic dividend (stated on top-income shares over years 0-7), decommodification, policy feedback, endogenous limits to redistribution, educated-youth unemployment; automatic stabilization now has an operational definition as the market-minus-disposable Gini gap.

  SUMMARY: Rising market-income inequality predicts graded democratic erosion among post-1990 democratizers (transitions 1989-1998) only where universal public health and education services built in the first democratic decade are thin; the gate's stabilization leg is measured directly as fiscal filtering (market-minus-disposable Gini gap), its behavioral legs as constituency formation and credible pre-commitment; the interaction is identified off welfare-specific trends; and the inequality-reduction leg of the democratic dividend materializes only behind the gate. The claim is a pre-registered prediction with fixed confirmation and disconfirmation criteria on public OWID panels; no estimates exist yet, and a null result would adjudicate for unconditional materialist or purely coalitional accounts.
motivation: >-
  The field currently holds two contradictory accounts of democratic erosion in the post-1990 wave. The materialist account
  (Houle 2009 for the coup era; Rau and Stokes 2025 for the erosion era) finds inequality is among the strongest predictors
  of democratic decline. The coalitional account (Haggard and Kaufman 2021) argues from close case analysis that economic
  grievances and inequality did not systematically distinguish post-1990 backsliders from survivors, and that polarization
  and elite coalitions did. This contradiction is unresolved because neither side tests the conditioning structure: Rau-Stokes
  estimate a global main effect on uninterrupted democracies with no welfare or education variables and no moderators; Haggard-Kaufman
  use case comparison without an interaction design. This hypothesis resolves the contradiction: inequality matters, but only
  where welfare institutions are too thin to absorb and convert it — both accounts are right in different institutional environments.
  It also extends Acemoglu, Naidu, Restrepo and Robinson's (2015) democratic-dividend result with a mechanism-level explanation
  of its failure: the inequality-reduction leg of the dividend is itself welfare-dependent, which explains why some new democracies
  consolidated and others — despite democratizing — never delivered the dividend and eroded. The finding is directly actionable:
  for post-1990 democratizers and any future democratization wave, the testable policy implication is that universal health
  and education systems must be built in the first democratic decade, before crises arrive. Everything is testable on public
  Our World in Data panels, making the study fully reproducible.
assumptions:
- >-
  The V-Dem Liberal Democracy Index (hosted on OWID) is a valid continuous measure of democratic quality for post-1990 democratizers,
  capturing the graded, executive-aggrandizement form of erosion rather than only discrete regime breakdown.
- >-
  Public health plus public education spending as a share of GDP, measured at the end of the first post-transition decade,
  is a valid pre-determined proxy for universalistic welfare institutions and is not itself determined by subsequent regime
  dynamics (measured before erosion onset).
- >-
  Cross-country comparability of the World Bank PIP Gini coefficient and the World Inequality Database top-10% income share
  is adequate for a country-year panel of post-1990 democratizers.
- >-
  The post-1990 democratization wave (1989-2005 transitions per V-Dem Regimes of the World / Boix-Miller-Rosato) provides
  quasi-exogenous transition timing, with welfare legacies (communist-era health and education systems, colonial-era public
  services) inherited rather than chosen by the new democracies.
- >-
  No unobserved confounder (EU accession, commodity rents, geographic region, initial GDP) drives both welfare-state strength
  and democratic resilience; this is probed by regional fixed effects, within-Eastern-Europe analysis, and placebo specifications.
investigation_approach: >-
  Build an OWID-only country-year panel, 1990-2022, of roughly 35-45 post-1990 democratizers (transitions 1989-2005 by V-Dem
  Regimes of the World), plus all democracies for comparison. Outcome: V-Dem Liberal Democracy Index (level and 5-year differences).
  Inequality treatment: lagged PIP Gini and WID top-10% income share. Welfare measure: WHO domestic general government health
  spending (% GDP) plus World Bank EdStats education spending (% GDP), set to their value at the end of the first democratic
  decade (pre-determined, time-invariant thereafter) — an intentionally non-cash, universal-services measure, contrasted against
  OECD SOCX total social spending (pensions-heavy) as a placebo moderator. Design: (1) two-way fixed-effects regressions with
  country and year fixed effects, interacting inequality with the pre-determined welfare measure — the gate test; (2) adjudication
  specification — baseline inequality effect without interaction (expected weak, matching Haggard-Kaufman) then with interaction
  (expected strong in the thin-welfare arm); (3) erosion-onset event studies with dynamic coefficients estimated separately
  by welfare arm, and lead-lag tests of whether public-services retrenchment and inequality surges precede liberal-democracy
  declines (sequencing vs. reverse causality); (4) democratization event study on inequality and public services by welfare
  legacy — the welfare-dependent dividend test; (5) mechanism arms: V-Dem polarization as mediator (inequality x thin-welfare
  -> polarization -> erosion) and ILO educated-youth-unemployment (education mismatch) as the second gate dimension; (6) robustness:
  alternative inequality measures, alternative welfare measures, population weights, exclusion of commodity booms, within-Eastern-Europe
  estimate, bootstrap confidence intervals for interaction terms. Implemented in Python (linearmodels/statsmodels, clustered
  standard errors), zero external data beyond OWID, no LLM spend.
success_criteria: >-
  CONFIRMATION requires: (a) a significant negative interaction between inequality and welfare strength on liberal-democracy
  trajectories — the within-country inequality effect is near zero (or positive) in the high-welfare arm and strongly negative
  in the thin-welfare arm, robust to all measure and sample swaps; (b) sequencing — inequality surges and public-services
  retrenchment lead liberal-democracy declines by 3-5 years in thin-welfare countries only, with no anticipatory welfare decline
  before erosion onset in the high-welfare arm; (c) the welfare-dependent dividend — democratization reduces the top-10% share
  only in high-welfare-legacy countries, and the size of the first-decade inequality-reduction dividend predicts 2010-2022
  resilience; (d) the mechanism arm — the inequality x thin-welfare interaction raises V-Dem polarization, and education-without-absorption
  (educated-youth unemployment) tightens the gate only where welfare is thin; (e) the universalism contrast — public services
  gate; OECD total social spending does not. DISCONFIRMATION: if the inequality effect is homogeneous across welfare arms
  (no gate), or the sequencing is reversed (erosion precedes welfare decline), or the interaction collapses once GDP level,
  region, and EU accession are controlled, then the hypothesis as stated is falsified — which would itself adjudicate in favor
  of unconditional materialist or purely coalitional accounts.
related_works:
- >-
  Rau and Stokes (2025, PNAS) 'Income inequality and the erosion of democracy in the twenty-first century': the flagship global
  demonstration that inequality predicts democratic erosion (1995-2020, 23 erosion episodes, uninterrupted democracies per
  Miller-Boix-Rosato). It contains no welfare-state or education variables and tests no moderation structure, and its sample
  excludes exactly the post-1990 democratizers that fell below the democracy threshold. This hypothesis adds the institutional
  gate, the young-democracy sample, and a continuous graded outcome.
- >-
  Houle (2009, World Politics) 'Inequality and Democracy: Why Inequality Harms Consolidation but Not Democratization': established
  inequality as a threat to democratic survival, but in a global sample across the coup-driven era with discrete survival
  outcomes and no welfare moderators. The hypothesis extends this to the graded-erosion era and conditions it on welfare institutions.
- >-
  Haggard and Kaufman (2021, 'Backsliding: Democratic Regress in the Contemporary World'): comparative case analysis arguing
  inequality and economic crises did not systematically distinguish post-1990 backsliders, with polarization and elite coalitions
  as proximate causes. The gate hypothesis offers the missing interaction design that can reconcile this with Rau-Stokes:
  inequality matters but only through thin welfare institutions — both accounts hold in different institutional environments.
- >-
  Acemoglu, Naidu, Restrepo and Robinson (2015, AER / NBER w19746) 'Democracy, Redistribution and Inequality': democratization
  raises schooling and public goods and reduces top-decile income shares on average. This hypothesis tests the unexamined
  conditionality of the inequality-reduction leg of that dividend on welfare institutions, and links the dividend's size to
  subsequent regime survival.
- >-
  Acemoglu, Johnson, Robinson and Yared (2005, AER) 'From Education to Democracy?': the load-bearing macro null that education
  does not cause democratization. This hypothesis does not contest the transition margin but moves to the resilience margin,
  where education operates through the welfare-service gate and the labor-absorption (mismatch) channel rather than through
  values socialization alone.
- >-
  Luehrmann (2021, Democratization) 'Disrupting the autocratization sequence': the conceptual framework of autocratization
  as a sequence (rule-of-law weakening, executive aggrandizement, accountability erosion) with institutional resilience as
  the disruptor, but no quantitative welfare-state test. This hypothesis quantifies one specific institution — the universal
  service welfare state — as the gate that disrupts the sequence.
- >-
  Szikra and Oektem (2023, JESP) 'An illiberal welfare state emerging? Welfare efforts and trajectories under democratic backsliding
  in Hungary and Turkey': documents how welfare states are transformed under backsliding (the outcome side). The hypothesis
  tests the opposite direction — whether welfare structure measured before erosion protects — with lead-lag tests that separate
  the two directions empirically.
- >-
  Vanhuysse (2006, 'Divide and Pacify'): strategic social policy as conscious demobilization of protest in early post-communist
  democracies. The hypothesis differs in mechanism (a structural gate on inequality shocks rather than strategic demobilization),
  in scope (the full post-1990 wave, three decades), and in outcome (graded democratic quality rather than protest quiescence),
  and explains the eventual failure of the gate in Hungary and Poland as cases with pension-heavy but service-thin welfare
  states.
- >-
  Campante and Chor (2012, QJE) 'Why Was the Arab World Poised for Revolution?': schooling interacted with poor economic opportunities
  predicts protest onset. The hypothesis transposes the mismatch mechanism from protest onset to graded democratic erosion
  across all post-1990 democratizers, and adds the welfare-state gate that Campante-Chor do not consider.
inspiration: >-
  Three cross-domain transfers structure the hypothesis. (1) Control theory — disturbance rejection: engineering asks what
  determines the gain with which an exogenous disturbance propagates to a state variable one cares about. Here the disturbance
  is the inequality shock, the state variable is democratic quality, and the welfare state is the feedback controller whose
  gain determines transmission; the empirical translation of 'disturbance rejection' is exactly the interaction (gate) design
  that this literature has not run. (2) Public-health effect modification: epidemiology does not ask only whether a risk factor
  harms, but whether modifiable protective exposures change the effect of exposure (clean water changes the effect of pathogens).
  The same logic — institutions as modifiable protective exposures that gate a socioeconomic risk factor's population-level
  harm — is standard in epidemiology but almost absent from the inequality-democracy literature, which estimates main effects.
  (3) Ecology's resistance-versus-resilience distinction: the fate of a disturbed system depends on its buffering capacity,
  not the disturbance alone; universal welfare institutions are the system's buffering capacity. The mechanism inside the
  gate is built from the reviewer's own theoretical toolkit — Acemoglu, Egorov and Sonin's (2013) populism equilibrium (elites
  endogenously limit redistribution, making populists' redistributive promises decisive) and Acemoglu-Robinson's democratization-as-commitment
  logic — combined with Esping-Andersen's decommodification and the policy-feedback insight that programs create their own
  defenders.
terms:
- term: Liberal Democracy Index
  definition: >-
    V-Dem's v2x_libdem index (0-1), combining electoral democracy with constraints on the executive and protection of civil
    liberties; hosted on Our World in Data; the outcome measure of democratic quality in this hypothesis.
- term: Post-1990 democratizers
  definition: >-
    Countries whose transition to electoral democracy began between 1989 and 2005, coded via V-Dem Regimes of the World and
    the Boix-Miller-Rosato regime classification; the treated sample of young democracies.
- term: Democratic erosion (backsliding)
  definition: >-
    Gradual, incremental decline in democratic quality — executive aggrandizement, weakened accountability, curtailed civil
    liberties — within a formally democratic regime, as opposed to sudden breakdown by coup.
- term: Welfare institutions
  definition: >-
    The universalistic service state: public health and public education spending as a share of GDP, which benefit broad segments
    of the population across the income distribution, as opposed to targeted cash transfers or pension-heavy social spending.
- term: Institutional gate (moderation)
  definition: >-
    The claim that the effect of one variable (inequality) on another (democratic quality) is conditional on a third (welfare
    institutions); the empirical expression is an interaction term, distinguishing this design from mediation-style 'through
    which channel' claims.
- term: Democratic dividend
  definition: >-
    The improvements in growth, schooling, public goods, and income distribution observed after democratization (Acemoglu
    et al. 2015); this hypothesis isolates the inequality-reduction leg and tests its dependence on welfare institutions.
- term: Decommodification
  definition: >-
    Esping-Andersen's concept: the degree to which welfare institutions sever living standards from labor-market position,
    so that market shocks are not immediately transmitted into citizens' welfare and political grievances.
- term: Policy feedback
  definition: >-
    The mechanism by which existing policies reshape politics — programs create constituencies with a material stake in preserving
    them, converting welfare beneficiaries into defenders of the public institutions democratic erosion would capture.
- term: Endogenous limits to redistribution
  definition: >-
    The Acemoglu-Egorov-Sonin (2013) result that high inequality induces elites to reduce redistribution strategically, so
    the median voter's demands go unmet and a populist promising redistribution can win — an equilibrium that universal automatic
    welfare programs pre-empt by committing redistribution in advance.
- term: Educated-youth unemployment
  definition: >-
    Unemployment among young people (15-24) with completed education, from the ILO Education and Mismatch Indicators on OWID;
    the operational measure of educational expansion without labor-market absorption.
summary: >-
  Rising inequality predicts democratic erosion among post-1990 democratizers only where welfare institutions are thin: universal
  public health and education systems built in the first democratic decade gate the inequality-erosion link, and the inequality-reduction
  'democratic dividend' of democracy itself materializes only behind that gate. Testable entirely on OWID panels, this welfare-gate
  account reconciles the global inequality-erosion finding (Rau-Stokes 2025) with the case-based skepticism about economic
  drivers (Haggard-Kaufman 2021) and explains which post-1990 democratizers consolidated and which backslid.
_relation_rationale: >-
  Same welfare-gate frame; refined to pre-fisc treatment, trend identification, earlier-transition cohort.
_confidence_delta: unchanged
_key_changes:
- >-
  Primary treatment switched to market-income inequality (WID pre-tax top-10% share; market Gini secondary); disposable-income
  Gini demoted to robustness because post-fisc Gini is post-treatment with respect to automatic stabilization (reviewer MAJOR:
  treatment-measure entanglement)
- >-
  Entanglement turned into mechanism test: the market-minus-disposable Gini gap now directly measures the automatic-stabilization
  (fiscal-filtering) leg of the gate
- >-
  Cohort restricted to transitions 1989-1998 so the first democratic decade ends before the 2008 crisis and precedes the 2010-2022
  resilience window; dividend window fixed at years 0-7; W measured at the earliest documented 3-year window with a T+3..7
  vs T+8..12 sensitivity pair making window drift visible (reviewer MAJOR: first-decade construct)
- >-
  Core identification now welfare-specific trends (W x t and W x t-squared): the gate must survive trend controls; staggered
  event studies use Callaway-Sant'Anna and Sun-Abraham estimators with pre-trend tests (reviewer MAJOR: differential trends)
- >-
  Exogeneity of W probed directly: W regressed on first-decade inequality dynamics and fiscal-collapse indicators; 2SLS on
  legacy instruments (communist-era schooling, colonial-era services); erosion-within-first-12-years cases dropped or recoded
  (reviewer MAJOR: exogeneity asserted not tested)
- >-
  Three mechanisms given discriminating implications (market-minus-disposable gap for stabilization; universal-vs-targeted
  composition and usage for constituency; program automaticity for pre-commitment); polarization arm demoted to a mechanism
  report since Rau-Stokes already invoke it (reviewer MEDIUM: mechanisms underdetermined)
- >-
  OECD-only total-social-spending placebo replaced by a full-sample transfer measure (ILO World Social Protection Database
  or IMF GFS) so the universalism contrast covers all retained countries (reviewer MAJOR: H5 coverage)
- >-
  Pre-registration commitments added: timestamped registry, primary-specification hierarchy, decision rule of p<0.05 in the
  primary spec plus at least 5 of 7 robustness cells, fixed country roster with coverage matrix, and simulation-based minimum-detectable-effect
  analysis at N=25-35 under rho 0.7-0.9 (reviewer MAJOR: low power; MAJOR: unregistered pre-registration)
- >-
  Novelty positioning added against Svolik 2015, Huber-Stephens 2001/2012, and Rothstein-Uslaner 2005; ANRR 2015 dividend
  claim corrected to top-income shares (reviewer MAJOR: missing prior work)
- >-
  Status reframed honestly: no models estimated yet, so the claim is a pre-registered prediction, not a finding; confirmation/disconfirmation
  criteria are fixed ex ante and a null result is counted as a contribution (reviewer MAJOR: no model estimated)
relation_type: evolution
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter2_dir1
type: dataset
objective: >-
  Construct the final, schema-validated OWID-only country-year panel (1985-2023 so event-study leads/lags are possible, all
  countries with regime flags) built exactly to the revised protocol. Deliverables: (a) fixed roster of post-1990 democratizers
  with transition T in 1989-1998, T dated from V-Dem Regimes of the World (v2x_regime, OWID-hosted) cross-checked against
  OWID's Boix-Miller-Rosato political-regime series, with per-country transition year, dating source, and first-democratic-decade
  windows documented; (b) PRE-FISC primary treatments: WID pre-tax national-income top-10% share (primary treatment) and the
  market-income Gini (secondary), disposable-income Gini retained as robustness only, plus a derived market-minus-disposable
  Gini gap column wherever both series exist with per-country-year coverage flags (this is the automatic-stabilization measure
  that turns the reviewer's entanglement objection into a mechanism test); (c) pre-determined gate W = WHO domestic general
  government health expenditure (% GDP) + World Bank EdStats government education expenditure (% GDP), measured at the EARLIEST
  available 3-year window within years 0-8 after transition with the actual calendar years documented per country, plus the
  T+3..7 and T+8..12 sensitivity values so window drift is visible; time-invariant thereafter; (d) placebo moderators: OECD
  total social spending (% GDP, flagged OECD-only) and any OWID-hosted full-sample social-protection/transfer series (ILO
  World Social Protection Database or IMF GFS; if absent on OWID, record the gap and the exact external source in the coverage
  matrix so the universalism contrast is not OECD-only); (e) mechanism series: V-Dem political polarization index and ILO
  educated-youth unemployment if OWID-hosted, otherwise the closest OWID ILO series with the gap explicitly recorded; (f)
  controls and auxiliaries: log GDP per capita, population, natural-resource rents (% GDP), region, EU-accession year, BMR
  democracy indicator. Emit raw per-series files, the merged panel, a per-country W snapshot table with actual calendar windows,
  the transition roster, a data dictionary with per-series source and OWID URL, and the coverage matrix (country x variable
  x window) as dataset metadata — all schema-validated with full/mini/preview JSON variants.
approach: >-
  Use the aii-owid-datasets skill to search and download the exact OWID catalog tables (V-Dem grapher tables for liberal democracy,
  electoral democracy, regime type, and polarization; WID inequality tables; PIP Gini tables by income concept; WHO health
  expenditure; EdStats education expenditure; OECD social expenditure; ILO labor-force and education-mismatch tables; GDP,
  population, natural-resource rents), standardizing on ISO3 country + year. Hand-code only the factual metadata OWID does
  not carry — transition dating from the regime series' first continuous democratic spell, and EU-accession year — with per-country
  documentation rows. Where a series is missing for the roster (EdStats 1990s gaps, WHO starting near 2000, ILO mismatch absence),
  record a gap row in the coverage matrix and DO NOT impute; the coverage matrix doubles as the reviewer-demanded 'country
  x variable x window' documentation and bounds the effective estimation sample per design. Where OWID exposes multiple variants
  of one concept (PIP vs WID Gini; income concepts within each), keep all variants and tag each as market / disposable / pre-tax
  so the experimenter can construct the market-minus-disposable gap unambiguously. Validate outputs against the exp-pipeline
  dataset schema and write full/mini/preview JSON variants.
depends_on: []
</artifact_direction>



<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>

<compute_profiles>
Choose the compute profile this artifact needs for execution.
Available profiles for dataset artifacts:
  - gpu: 1x NVIDIA RTX A4500, 20GB VRAM, 7 vCPUs, 29GB RAM — ML training, CUDA, large models (fallback: GPUs cheap→expensive: 2000 Ada → A4000 → 4000 Ada → L4 → 4090 → 5090)
  - cpu_heavy: 4 vCPUs, 32GB RAM — large datasets, memory-intensive processing (fallback: CPUs cheap→expensive, then GPU hosts cheap→expensive (all ≥32GB RAM))

Set runpod_compute_profile to one of these exact tier names.
</compute_profiles>
GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/user_uploads`. Check this folder for anything relevant to your task. It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for a DATASET artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-05 11:36:26 UTC

```
Direction: Comparative Political Economy — Inequality and Democratic Resilience. Something genuinely novel and groundbreaking that traces how inequality, education, and democratic-quality co-evolve across post-1990 democratizers, identifies what sustains resilience versus backsliding, and tests whether welfare-state institutions mediate the link. MUST use Our World in Data (OWID) panels.

Ambition: level 1 of 5 — confirmatory/parametric science: a careful confirmatory test within established institutional-economics theory; precision, identification, and robustness over conceptual novelty.

Reviewer: I am Daron Acemoglu (MIT). Calibrate from my existing work. Cross-domain perspectives (historical sociology, political behavior, economic anthropology) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for the American Political Science Review, the Journal of Democracy, or World Politics. Audience: comparative political economists and political scientists. Tone: empirically rigorous, grounded in institutional economics, reproducible on public OWID data.
```

### [3] SKILL-INPUT — aii-owid-datasets · 2026-09-05 11:37:24 UTC

The agent loaded the **aii-owid-datasets** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-owid-datasets
description: "Searches and downloads country-and-year statistical tables from the Our World in Data (OWID) catalogue — energy, climate, health, COVID-19, economics, environment, demographics — returning real rows plus variable metadata as full, mini and preview JSON. Use whenever a task needs real-world global or per-country indicator data, national time series, or a specific OWID grapher or garden table path. Triggers: Our World in Data, OWID, owid.catalog, grapher or garden table path, global statistics, per-country time series, CO2 emissions, life expectancy, population, energy mix, GDP and development indicators. NOT for: machine-learning training or benchmark datasets on the HuggingFace Hub, which aii-hf-datasets covers; JSON schema validation, which aii-json covers; rendering the chart, which aii-data-fig-gen covers."
---

## Contents

- Workflow (2-phase table discovery process)
- Scripts (Search, Download with full parameters)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Workflow: 2-Phase Table Discovery

### Phase 1: Search for Tables
Find tables with metadata (title, description, variables)
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_search_datasets.py "renewable energy" --limit 5
```

### Phase 2: Download Table (if suitable)
Download the table after reviewing the search results
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_download_datasets.py "grapher/energy/2023-12-12/energy_mix"
```

---

## Scripts

### Search OWID tables (aii_owid_search_datasets.py)

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_search_datasets.py "climate change" --limit 3
```

**Parallel execution (multiple queries):**

IMPORTANT: When running multiple searches, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_owid_search_datasets.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {} --limit 3' ::: 'renewable energy' 'climate change' 'covid mortality'
```

**Example output:**
```
Found 3 OWID tables for 'climate change':

[1] Climate Change Impacts
    Path: grapher/climate/2023-10-15/climate_impacts
    Description: Global temperature anomalies and sea level rise...
    Variables (42 total):
      - Global temperature anomaly (°C): Annual global mean temperature anomaly
      - Sea level rise (mm): Global mean sea level change
      - Atmospheric CO2 concentration (ppm): Monthly CO2 concentration at Mauna Loa
      - Arctic sea ice extent (million km²): Monthly Arctic sea ice extent
      ...
```

**Parameters:**

`query` (required, positional)
- Search query string
- Examples: `"covid"`, `"energy mix"`, `"climate change"`

`--limit` (optional)
- Number of search results to return (default: 3)
- Higher values = more results to choose from

**Tips:**
- Search queries the OWID catalog index via ``owid.catalog.search`` (network required;
  the catalog is cached after the first call, which the worker warms at init)
- Returns metadata only - no data is downloaded
- Use the `path` field from results to download specific tables
- Ranking and matching are the catalog's own (fuzzy by default) across table titles,
  descriptions and paths
- Search returns tables from all channels (garden=highest quality, meadow=raw, backport=legacy, open_numbers=Gapminder)

---

### Download OWID table (aii_owid_download_datasets.py)

Download a table by path (from search results) and save to files.

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_owid_download_datasets.py "grapher/energy/2023-12-12/energy_mix"
```

**Parallel execution (multiple tables):**

IMPORTANT: When downloading multiple tables, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-owid-datasets" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_owid_download_datasets.py" && \
parallel -j 50 -k --group --will-cite '$PY $S {}' ::: 'grapher/energy/2023-12-12/energy_mix' 'grapher/demography/2023-10-10/population' 'grapher/health/2023-08-01/life_expectancy'
```

**Example output:**
```
Downloaded OWID table: grapher/energy/2023-12-12/energy_mix

Dimensions: 15,420 rows x 12 columns
Columns: country, year, coal, oil, gas, nuclear, hydro, solar, wind, biofuels...

Files saved:
  Mini (READ THIS for development/testing): /path/to/mini_grapher_energy_2023-12-12_energy_mix.json
  Preview (DO NOT READ - for logging only): /path/to/preview_grapher_energy_2023-12-12_energy_mix.json
  Full (DO NOT READ - for scripts only):    /path/to/full_grapher_energy_2023-12-12_energy_mix.json

Sample data (first 3 rows):
  Row 1:
    country: Afghanistan
    year: 2000
    coal: 0.5
    ...
```

**Parameters:**

`path` (required, positional)
- Table path from search results
- Examples: `"grapher/energy/2023-12-12/energy_mix"`, `"garden/demography/2023-10-10/population"`

**Output files (auto-saved to `temp/tables/`):**
1. **Mini**: `mini_{path}.json` - 3 full rows - **READ THIS** for development/testing
2. **Preview**: `preview_{path}.json` - 3 truncated rows - **DO NOT READ directly** - for code you write to read
3. **Full**: `full_{path}.json` - All rows - **DO NOT READ directly** - for code you write to read

**Tips:**
- **Critical**: Only read the mini file directly with Read tool. Preview and full are input paths for code you write
- Use the `path` from search results to download specific tables
- Downloads directly from OWID catalog (network required)
- Files always saved to `temp/tables/` (path included in response)

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [4] SKILL-INPUT — aii-json · 2026-09-05 11:37:24 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: "Validates JSON files against this repo's experiment-pipeline schemas (exp_sel_data_out, exp_gen_sol_out, exp_eval_sol_out, exp_proof_out) and generates size-optimized full, mini and preview variants of any JSON array file. ALWAYS use before treating a pipeline stage output as finished, whenever a schema or required-property error must be fixed, and whenever a large JSON file needs a small truncated version safe to read. Triggers: JSON schema validation, schema compliance, required property errors, pipeline stage outputs, the exp_*_out format names, mini and preview JSON generation, shrinking a large JSON before inspection. NOT for: discovering or downloading new datasets, which aii-hf-datasets and aii-owid-datasets cover; splitting oversized output files, which aii-file-size-limit covers; plotting JSON data, which aii-data-fig-gen covers; spreadsheet and .csv tabular data, which anthropic-xlsx covers."
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Experiment Pipeline** — the four formats `schemas/` actually holds and
`AVAILABLE_FORMATS` in `scripts/aii_json_validate_schema.py` accepts (this
list used to name six hypothesis-selection schemas that exist nowhere and
omit the proof one; corrected 2026-09-03):
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format
- `exp_proof_out.json` - Experiment Proof format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-web-tools · 2026-09-05 11:38:40 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````
