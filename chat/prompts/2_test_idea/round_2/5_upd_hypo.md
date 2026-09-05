# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_2nz_vV2E7aIl` — The Welfare Gate: Pre-Fisc Inequality, Universal Public Services, and Democratic Resilience in Post-1990 Democratizers
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-09-05 12:16:38 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

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
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

No artifacts yet.
</all_artifacts>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# The Welfare Gate: Pre-Fisc Inequality, Universal Public Services, and Democratic Resilience in Post-1990 Democratizers

*A pre-registered research design. No model has been estimated; the estimates do not exist yet. The protocol, the fixed country roster, the coverage matrix, and the power analysis are deposited in a timestamped registry (OSF; the registration ID and deposit date are fixed at the moment of deposit) before any estimation. This paper states the theory, the data infrastructure, the six pre-committed estimation designs, and the decision rules against which results will be judged. It is written for venues that publish registered designs and pre-analysis plans; we do not report estimates because none are in hand.*

## Abstract

The literature on democratic erosion in the twenty-first century holds two contradictory accounts. The materialist account finds that income inequality is among the strongest predictors of democratic decline in a global sample of uninterrupted democracies [1]. The coalitional account argues, from close case comparison, that economic grievances did not systematically separate post-1990 backsliders from survivors [2]. This paper argues that the contradiction is unresolved for a structural reason: neither account tests the conditioning structure, and the statistical account's treatment is entangled with the very institution the gate hypothesis implicates. Disposable-income inequality is post-fisc, and fiscal systems that compress it are larger where welfare states are larger, so a gate estimated on the disposable Gini cannot separate institutional transmission from arithmetic filtering. We register a design that corrects both problems: the treatment is pre-fisc, the World Inequality Database pre-tax top-10 percent income share, with the market-income Gini secondary. The fiscal filter is measured directly as the market-minus-disposable Gini gap, converting the entanglement into the test of the stabilization mechanism. Among post-1990 democratizers whose transition began between 1989 and 1998, the hypothesis is that market-inequality surges erode the V-Dem Liberal Democracy Index three to five years later only where universal public health and education services built in the first democratic decade are thin. The gate is identified off deviations from welfare-specific trends, with estimators built for differential treatment timing, a fixed roster with a documented coverage matrix, and a simulation-based minimum-detectable-effect analysis. Confirmation and disconfirmation criteria are fixed ex ante, with a primary-specification significance rule and a five-of-seven robustness threshold. The design is built so the test can adjudicate between unconditional materialist, purely coalitional, and institutionally gated accounts.

## 1. Introduction

Since the late twentieth century the main threat to democratic regimes has changed character. The military coup has given way to the power-aggrandizing elected executive: presidents and prime ministers who capture courts, harass the press, and de-legitimize elections [1, 3, 4, 5]. Erosion is now understood as a graded, incremental process inside formally democratic regimes, and a third wave of autocratization is dated to the late 2000s [6]. The process descends from national executives to state governments [7]. The question that dominated twentieth-century comparative politics, what kills democracies, has been replaced by a harder one: how much democratic quality does a regime lose, and which democracies lose almost none?

Two answers compete. The materialist account points to income inequality. In a cross-national sample of democracies that remained uninterrupted over 1995-2020, Rau and Stokes count 23 spells of backsliding in 22 countries, lasting nine years on average, and find that the Gini coefficient is among the strongest predictors of erosion onset [1]. The result extends an older one: in the coup era, inequality harmed democratic consolidation even where it did not block democratization [8], in line with the distributional-conflict tradition in which redistribution is the pivot of regime conflict [9, 10, 11]. The coalitional account pushes back. From close comparison of the post-1990 wave, Haggard and Kaufman conclude that economic grievances and rising inequality did not systematically separate backsliders from survivors; polarization and elite coalitional choices did [2, 12]. One literature says inequality is a central driver of erosion. Another says the economic story fails exactly in the cases that matter.

Both claims cannot hold in the unconditional form in which they are stated. The dispute has not been resolved because neither side runs the design that could resolve it. The statistical account estimates a main effect: its specifications contain no welfare variables and no moderators, and its sample of uninterrupted democracies excludes precisely the young democratizers that fell below the democracy threshold while eroding [1]. The case-based account compares backsliders with survivors but never formalizes the interaction structure a conditional claim requires [2]. What is missing in both is the institutional environment, and in the statistical account there is a deeper problem. Rau and Stokes measure inequality with disposable-income Ginis and with World Inequality Database shares that are pre-tax [1]. Disposable income is post-fisc. In any country the fiscal system compresses market inequality, and the compression is larger where public services and transfers are larger. A specification that uses the disposable Gini as the treatment, with no welfare variables, cannot separate "inequality erodes democracy" from "fiscal systems that compress inequality also protect democracy." The first mechanism of any welfare-gate account, automatic stabilization, is built into the treatment of the very paper that establishes the unconditional result.

This paper registers a design that corrects both problems and states the gate hypothesis plainly. Among post-1990 democratizers whose transition to electoral democracy began between 1989 and 1998, a rise in market-income inequality, measured pre-fisc, erodes liberal-democratic quality three to five years later only where welfare institutions built in the first democratic decade are thin. In countries whose first democratic decade universalized public health and education into services the broad middle class actually uses, market-inequality surges do not transmit into declines in the Liberal Democracy Index; where public services stayed thin, the same surges predict graded erosion. The gate decomposes into two paths, and the design measures them separately. Automatic stabilization is the fiscal filter: the market-minus-disposable Gini gap, the share of any market shock that the fiscal system absorbs before it reaches the distribution citizens experience. Behavioral transmission is the residual link from the market shock citizens do experience to democratic quality, gated by constituency formation, by which the middle class holds a material stake in the public institutions erosion would capture [13, 14, 15], and by credible pre-commitment, by which universal automatic programs block the elite-retrenchment and populist-promise equilibrium of Acemoglu, Egorov, and Sonin [16]. The gate is the universal service state, not welfare effort in general: pension-heavy total social spending, targeted cash, and chauvinist transfers do not gate, and generosity purchased later by incumbents is part of the erosion playbook, not a substitute [17, 18, 19, 20, 21].

Why has this design not been run before? Three literatures hold its parts, and none has assembled them. The welfare-state literature established the concepts the gate needs: decommodification, by which welfare institutions sever living standards from labor-market position [22]; the paradox of redistribution, by which universal programs redistribute more than targeted ones [23]; and policy feedback, by which programs create their own defenders [13, 14]. The democratic-dividend program established that democratization raises tax revenues and schooling, and found no robust average effect on inequality, with imprecise estimates on net and gross Gini coefficients and suggestive heterogeneity by land inequality and structural transformation [24]. The erosion literature measures neither welfare institutions nor the post-1990 cohort's conditional structure [1, 2]. The closest existing statements of the gate's logic are the finding that young democracies are distinctively vulnerable to incumbent takeover rather than coups [25], the argument that welfare states underwrite democratic legitimacy and consolidation in Latin America [26, 27], and the universalism-to-trust microfoundation of institutional legitimacy [15]. Each stops short of the inequality-shock interaction structure this design estimates.

The status is stated plainly because it matters for how the paper is read. No model has been estimated. This is a pre-registered research design: the roster, the coverage matrix, the six estimation designs, and the decision rules in Section 6 are fixed and deposited before estimation. We present the theory, the data infrastructure, and the protocol; a companion paper will report estimates against the Section 6 criteria. The design is restricted to public Our World in Data (OWID) panels [28], with one disclosed non-OWID input, the Boix-Miller-Rosato cross-check for transition dating [29]; every variable is downloadable by any reader, and the full analysis is reproducible without proprietary data. Figure 1 diagrams the gate.

[FIGURE:fig1]

**Summary of contributions.** (i) We reconcile the materialist and coalitional accounts of post-1990 erosion by identifying the institutional condition under which each holds: inequality erodes democracy where welfare institutions are thin, and the coalitional story dominates where they are thick. (ii) We correct the measurement entanglement that has biased the materialist account toward a spurious unconditional effect: the treatment is pre-fisc, and the fiscal filter is measured directly as the market-minus-disposable Gini gap, so the stabilization mechanism is tested rather than assumed. (iii) We condition the inequality leg of the democratic dividend on welfare institutions [24], state the dividend on top-income shares over a fixed post-transition window, and link its size to regime resilience two decades later. (iv) We identify the gate off deviations from welfare-specific trends, with estimators designed for differential treatment timing [30, 31], exogeneity probes on the pre-determined welfare measure, and a fixed roster with a documented coverage matrix, so the confirmation criteria are calibrated to the power the sample can actually deliver.
## 2. The Two Accounts and the Missing Interaction

### 2.1 The materialist account

Rau and Stokes identify erosion spells using expert-survey measures of decline in vertical and horizontal accountability, coded from V-Dem information [1]. Between 1995 and 2020 they count 23 spells of backsliding in 22 countries, lasting nine years on average. The unit of analysis is the country-year, and inclusion requires a country to have been an uninterrupted democracy over the period under the Miller-Boix-Rosato classification; the main analyses cover 92 countries, with Venezuela the single admitted case that eroded into autocracy [1, 29]. The leading predictor is the Gini coefficient, and the calibration is stark. For Sweden, whose Gini of 26.4 in 2017 makes it more equal than 87 percent of democracies, the predicted annual risk of erosion is 4 percent. For the United States, whose Gini of 38.4 exceeds that of 60 percent of democracies, the predicted risk is 8.4 percent. South Africa, the most unequal democracy in the sample, has a predicted risk of 31 percent [1]. The result extends to the structure of inequality: the larger the income and wealth shares of the top 1 and top 10 percent, the more likely democracy is to erode, and the larger the bottom-half share, the less likely [1]. The association survives a wide battery of alternatives: four Gini sources, wealth inequality, country-year and country-election-year units, rare-events estimation, and region and country fixed effects [1].

Two details of that paper matter for this one. First, the top-end income and wealth shares come from the World Inequality Database, and those shares are pre-tax [1]. The flagship result's structural measures are already market-income in concept, while its Gini measures are post-fisc, and the design estimates a single main effect pooling both. Second, Rau and Stokes interpret the channel through polarization: their mechanism analysis uses a measure of affective polarization, with V-Dem's societal polarization as the robustness alternative [1, 12]. The gate account does not contest that polarization is the proximate channel; it contests the claim that polarization is a sufficient channel, because the polarization-to-erosion link is exactly what universal service institutions are hypothesized to interrupt. We return to this in Section 3 and pre-commit the differentiating reading in Section 6.

The account's lineage matters for what it does not test. Houle's result, that inequality harms democratic consolidation but not democratization, was estimated in a global sample across the coup-driven era with discrete survival outcomes [8]. Haggard and Kaufman's earlier statistical work likewise found inequality among the correlates of democratic instability [32]. The theoretical tradition behind both is the distributional-conflict model of regimes, in which democratization is a commitment device that elites accept when the revolution constraint binds, and the redistributive threat it poses is what makes elites resist [9, 10, 11]. In that tradition inequality is the central cause, and welfare policy is a consequence of democracy, not a condition on its survival.

### 2.2 The coalitional account

Haggard and Kaufman's comparative work on the post-1990 wave reaches a different conclusion [2, 33]. Backsliders such as Hungary, Poland, Turkey, and Venezuela, and survivors such as the Baltic states, Slovakia, South Korea, and Chile, do not separate cleanly on economic grievances. Some backsliders grew rapidly and reduced poverty; some survivors suffered deep crises. What distinguishes the two groups, in their reading, is the configuration of elites and parties: whether the political system produced a dominant coalition with incentives to dismantle constraints, and whether polarization gave that coalition an electorally sustainable base [2, 12]. Their empirical strategy is comparative case analysis, and they are explicit that the economic variables that dominate the statistical literature do not carry the explanatory weight in the cases [2]. Bermeo's conceptual history and Waldner and Lust's synthesis stress steady, incremental, often stealthy executive aggrandizement as a political choice rather than an economic reflex [3, 4]. Lührmann's account of autocratization as a sequence locates the disruptive potential in institutional resilience, the general phenomenon of which the welfare state is, in our account, a specific instance [34].

### 2.3 Prior conditioning results

Three bodies of work already touch the conditional structure the gate needs, and each stops short of it. We state the differences now because the gate's contribution is defined against them.

**Young democracies are the population at risk.** Svolik shows that young democracies are vulnerable to incumbent takeovers rather than coups, and that consolidation is slow: most democratic failures in the postwar era are executive power grabs in countries that have not yet experienced successful alternations in power [25]. This defines the population this paper studies, the post-1990 cohort, and the outcome class, executive-aggrandizing erosion. Svolik conditions the risk on the history of electoral contestation, not on welfare institutions, and his framework does not engage the inequality channel at all. The gate adds exactly that: within the young-democracy population, the inequality-erosion link is conditional on the service state built in the first democratic decade.

**Welfare states underwrite democratic legitimacy and consolidation.** Huber and Stephens argue, from Latin America and from the advanced democracies, that welfare states provide legitimacy to democratic institutions and that their development and crisis track the fate of democracy [26, 27]. This is the closest existing statement of the gate's constituency logic. It differs from the gate in three ways: it is about average legitimacy rather than the effect of inequality shocks; it does not test an interaction between welfare structure and inequality movements on democratic trajectories; and its consolidation accounts concern longer-lived democracies, not the post-1990 cohort with its inherited service legacies.

**Universalism produces the legitimacy that protects institutions.** Rothstein and Uslaner establish the microfoundation: universal welfare institutions generate equality, equality generates generalized trust, and trust generates support for institutions [15]. The gate's constituency-formation mechanism is this argument applied at the margin of an inequality shock: universal services give the middle class a material stake in the public institutions that erosion would capture, so the institutions themselves acquire defenders [13, 14, 15]. The gate claims effect modification, a conditional claim none of these works tests.

### 2.4 The missing interaction and the dividend's null leg

Neither leading account tests the conditioning structure. The statistical account has no interaction terms: its specifications include no welfare variables, so it cannot observe whether the inequality coefficient is carried by the thin-welfare democracies in its sample, and its sample restriction excludes exactly the case population that matters most for adjudication, the young democratizers that fell below the democracy threshold while eroding [1]. The case-based account has an interaction design in substance, backsliders versus survivors across institutional environments, but no welfare measure is coded systematically and no statistical claim about effect modification is made [2]. The two accounts are not in fact rivals at the level of their designs. They are main-effect and case-descriptive enterprises, each silent on the dimension that would separate them.

A third literature makes the conditional structure concrete, and its own null marks the place where the gate should sit. The democratic-dividend program established that democratization has a robust effect on tax revenues, about a 16 percent long-run increase in the tax-to-GDP ratio in the preferred specification, and on secondary schooling and structural transformation, but no robust average effect on inequality [24]. The chapter's inequality analysis runs net and gross Gini coefficients and top- and bottom-income shares relative to the middle; some specifications show negative effects on inequality, especially on the gross Gini, but the estimates carry large standard errors and are not stable, and the heterogeneity it reports, by land inequality, structural transformation, and the top-bottom share structure, is suggestive rather than robust [24]. We cite the chapter for what it reports: imprecise average estimates, not a robust top-share decline. The field fact to explain is therefore not why inequality fails to fall on average, but under what conditions it does fall and whether that condition also gates erosion. The gate hypothesis supplies one candidate condition, welfare institutions, and the design in Section 5 makes the dividend conditional in exactly the way the chapter's own conclusion invites: it calls for a systematic investigation of the conditions under which democracy reduces inequality [24].

The outcome-side literature sharpens the direction of the test. Szikra and Öktem document how welfare states are transformed under democratic backsliding in Hungary and Turkey, converting universal or semi-universal systems into instruments of the illiberal project [17]. Lendvai-Bainton and Szelewa trace the same conversion in Hungary and Poland's radical welfare reforms [18]. Vanhuysse reads early post-communist social policy as strategic demobilization of protest [19]. Benczes and Orzechowska-Wacławska document how populist governments used economic policy, including family allowances and tax favors, to consolidate their coalitions [20], and Ennser-Jedenastik shows that welfare chauvinism is a standard plank of populist radical-right platforms [21]. These works study welfare as an outcome of backsliding. This paper tests the opposite direction, whether welfare structure measured before erosion protects, with lead-lag tests that separate the two directions empirically.

The design gap is now precise. What the inequality-democracy literature has never done is to estimate the effect of a market-income inequality shock on democratic quality as a function of welfare institutions that preceded the shock, with a treatment that is not itself compressed by those institutions. Section 3 states that hypothesis; Section 4 builds the data; Section 5 fixes the estimation; Section 6 fixes the decision rules.
## 3. Theory and Hypotheses

### 3.1 The gate and its two paths

The gate claim is a claim about effect modification, and the entanglement problem reviewed in Section 2 forces the claim to be stated on the right treatment. Let $m_{it}$ be market (pre-fisc) inequality in country $i$ and year $t$, let $d_{it}$ be disposable (post-fisc) inequality, and define the fiscal filter as the gap $g_{it} = m_{it} - d_{it}$. The gap is the share of market inequality that the fiscal system removes before the distribution reaches citizens. It is not a nuisance: it is the first mechanism of the gate, automatic stabilization, made visible. A market shock of size $\Delta m$ produces a disposable shock of size $\Delta d = (1 - \phi(W)) \Delta m$, where $\phi(W)$ is the filter, increasing in the scale and progressivity of the welfare state $W$.

The total effect of a market shock on liberal-democratic quality decomposes into two terms:

$$\frac{d \text{LibDem}}{d m} = \underbrace{\frac{\partial \text{LibDem}}{\partial d} \big(1 - \phi(W)\big)}_{\text{fiscal filtering}} + \underbrace{\frac{\partial \text{LibDem}}{\partial m}\Big|_{\bar d}}_{\text{behavioral transmission}},$$

where the first term is arithmetic: it operates even if no citizen changes any behavior, because less of the shock reaches the distribution politics responds to. The second term is the behavioral residue: the effect of the market shock on democratic quality holding the disposable path fixed, gated by constituency formation and credible pre-commitment. A research design that treats $d$ as the treatment and $W$ as the moderator conflates the two terms. A design that treats $m$ as the treatment and measures $g$ directly separates them. This paper registers the second design. Under the arithmetic-only account, the residual market effect is homogeneous in $W$ once $g$ is controlled, and the gate interaction disappears when the gap enters the specification. Under the behavioral account, the interaction survives gap control. Section 6 fixes which of these readings each pattern of results supports.

A simple sketch disciplines the functional form. Two periods. In period 0, the first democratic decade, society operates a universal service state of size $w$: services that a share $u(w)$ of households use, with $u' > 0$ and $u'' < 0$. In period 1, a market shock raises $m$, and a populist incumbent offers erosion: erosion delivers a private benefit $B$ to the executive and captures the public services, worth $\lambda w$ to each user household. Household $h$ supports erosion if its grievance $g_h(d) + v_h$ exceeds its stake, where $d = (1 - \phi(w)) m$, grievance is increasing and convex in experienced inequality ($g' > 0$, $g'' > 0$), and $v_h$ is the fear of elite capture in the sense of Acemoglu, Egorov, and Sonin, shifted up where inequality is high [16]. Erosion proceeds if supporters cross a threshold. The marginal effect of the market shock on the erosion hazard is $\beta(w) = \gamma(1 - \phi(w)) - \delta u'(w) - \kappa A(w)$, where $\gamma$ is the grievance channel, $\delta u'(w)$ is the constituency channel, and $\kappa A(w)$ is the pre-commitment channel, with $A(w)$ indexing program automaticity. With $\phi$ convex and $u$ concave, $\beta'(w) < 0$ and $\beta''(w) > 0$: the gate exists, and protection is diminishing, so the marginal-effect curve is convex and threshold-like rather than linear. The sketch is a heuristic, not a structural model; its role is to discipline the functional forms reported in Section 6. We pre-commit to estimating the interaction linearly and with a quadratic term, and to plotting the inequality marginal effect at welfare-distribution percentiles so a threshold shape is visible if it is there. Figure 2 diagrams the decomposition.

[FIGURE:fig2]

### 3.2 Three mechanisms and their discriminating implications

**Automatic stabilization.** Universal public services sever household welfare from labor-market position. Public health care keeps medical costs off household budgets when earnings fall; public education keeps the next cohort's human capital accumulation independent of parental income shocks. This is decommodification applied to the post-1990 wave [22], and its operational measure is the one the entanglement problem already produced: the market-minus-disposable Gini gap. The mechanism is direct, so its discriminating implication is direct. If the gate interaction is fully explained by the gap, that is, if including the gap and its interaction drives the residual inequality-by-welfare interaction to zero, stabilization is the entire mechanism. If the interaction survives gap control, a behavioral residue exists and must be attributed to the next two mechanisms.

**Constituency formation.** Programs create their own defenders [13, 14]. When the broad middle class uses public health and public education daily, it holds a material stake in those institutions: their quality, their budgets, their autonomy from the executive. Erosion threatens exactly that. An executive who captures the health ministry or the school system captures a service a household depends on, and a middle class that perceives the capture as a loss of a valued public asset has a concrete, self-interested reason to resist. The microfoundation is the universalism-to-trust-to-legitimacy chain of Rothstein and Uslaner [15], applied at the margin of an inequality shock. The mechanism does not require civic virtue. It requires that the middle class has something at stake in the public sector. The discriminating implications: the gate should not exist where the welfare state is pension-heavy or means-tested, because the middle class is not enrolled; and the interaction should attenuate when spending composition, the share of public services in total social spending, and usage proxies are controlled.

**Credible pre-commitment.** When inequality is high, voters anticipate that elites will respond to redistributive threats by limiting redistribution, and the median voter's demands go unmet; a populist who credibly promises redistribution can then win without being able to deliver it [16]. Universal, automatic welfare programs pre-commit redistribution in advance: the institutional structure delivers services as a matter of routine, so the redistributive promise is not the exclusive property of an insurgent. The gate blocks the populist-promise equilibrium at its source, by removing the unmet demand that makes the promise decisive. The discriminating implication: the gate should be stronger where services are automatic, entitlement-based, indexed, and non-discretionary, and absent where generosity is discretionary and late-bought. The outcome-side literature has already documented the second half of this pattern, that incumbents under erosion expand targeted and chauvinist transfers while dismantling services [17, 18, 19, 20, 21]; the design tests whether that late-bought generosity substitutes for the gate, which the hypothesis says it does not.

The three mechanisms share one implication that H5 states as a contrast: what gates is the universal service state, not welfare effort in general. Targeted cash transfers do not stabilize automatically, because they are discretionary; they do not enroll the middle class, because they are means-tested; and they do not pre-commit, because an incumbent can redirect them at will. Pension-heavy spending enrolls the elderly, not the young and the employed, and it is the component that distinguishing politicians can expand while dismantling services. Late-bought generosity is worse than neutral: it buys quiescence while institutions are dismantled.

### 3.3 The co-evolution of inequality, education, and democracy

The gate also explains a second set of facts: the co-evolution of inequality, education, and democratic quality in the post-1990 wave. Democratization has a robust effect on tax revenues and schooling but no robust average effect on inequality [24]. The field fact, stated precisely in Section 2, is that the inequality-reduction leg of the democratic dividend does not materialize on average. The gate account explains why: fiscal expansion reduces inequality only where universal service institutions are strong enough to convert resources into distributional change and to keep leakage low. In thin-welfare democratizers, higher taxation without service delivery produces neither redistribution nor a middle-class constituency attached to public provision. The first-decade dividend, or its absence, then connects democratization to its own fate: countries whose first democratic decade delivered a visible, universal dividend entered the crisis years with a welfare buffer and a service constituency; countries where it did not entered them without either.

Education operates through the same institutional channel. The macro evidence that education causes democratization is weak [35], and the gate account agrees at the transition margin. At the resilience margin the channel is different: education builds democratic resilience when it is absorbed into middle-class employment and enrolled in public services, because both give the educated a stake in the existing order. Where education expands without absorption, the Campante-Chor mismatch operates, schooling combined with poor economic opportunities producing grievances and mobilization, transposed here from protest onset to graded erosion [36]. The redistributive politics of education [37] and the cleavage structures documented by Gethin, Martinez-Toledano, and Piketty [38] are the microfoundations of that channel. The hypothesis therefore predicts that education-without-absorption tightens the gate only where welfare is thin: the mismatch arm of the design.

### 3.4 Hypotheses

The theory yields five pre-registered hypotheses. Each is stated with its discriminating implication so that a confirming result can say which mechanism did the work, and a disconfirming result can say which account survives.

**H1 (the gate).** The within-country effect of a lagged market-inequality increase on the Liberal Democracy Index is negative and substantively large in thin-welfare countries and near zero or positive in strong-welfare countries; equivalently, the interaction of pre-fisc inequality with pre-determined welfare strength is positive and significant, under welfare-specific trend controls. The functional-form report pre-committed in Section 3.1 distinguishes a linear from a convex, threshold-like gate.

**H2 (sequencing).** Market-inequality surges and public-services retrenchment lead liberal-democracy declines by three to five years in thin-welfare countries, and no anticipatory service decline precedes erosion onset in high-welfare countries. The temporal order distinguishes the gate from the reverse-causal story in which erosion causes welfare decline [17].

**H3 (the welfare-dependent dividend).** Democratization reduces the top-10 percent income share, producing an inequality-reduction dividend over the first post-transition years, only in high-welfare-legacy countries; the size of that first-decade dividend predicts 2010-2022 resilience.

**H4 (mechanisms).** At least one discriminating mechanism result obtains: (a) the interaction attenuates toward zero once the market-minus-disposable gap and its interaction are controlled, supporting stabilization; (b) the interaction attenuates once spending composition and usage proxies are controlled, supporting constituency formation; (c) the interaction is stronger where services are automatic and absent for discretionary late-bought transfers, supporting pre-commitment; (d) the inequality-by-thin-welfare interaction raises V-Dem polarization, and education-without-absorption tightens the gate only where welfare is thin, consistent with the proximate-channel account in which universal institutions interrupt the polarization-to-erosion link that Rau and Stokes document [1]. Arms (a) through (c) discriminate among the gate's own mechanisms; arm (d) is a mechanism report placed in the proximate channel that the rival account already occupies, and its failure would not falsify the gate.

**H5 (universalism contrast).** The gate is produced by public services, health and education spending, not by total social spending, pension-heavy and transfer-dominated, and not by generosity acquired later through targeted or chauvinist transfers [17, 18, 19, 20, 21]. Total social spending and late-bought transfers are placebo moderators: they do not gate.

The corollary states the asymmetry precisely. Welfare institutions built in the first democratic decade, before crises arrive, gate the inequality-erosion link. Welfare generosity purchased later by incumbents is not a substitute; it is part of the erosion playbook. Temporal priority of universal institution-building, not the level of welfare effort, is what protects. The cohort restriction to transitions beginning by 1998, the welfare window defined inside the first democratic decade, and the exclusion of cases whose erosion began within the first twelve years all operationalize the priority claim, so that the pre-determined precedes the outcome it is used to explain.
## 4. Data and Measurement

The design is restricted to public OWID panels [28]. OWID aggregates the underlying primary sources: V-Dem for regime and outcome measures [39, 40], the World Bank's Poverty and Inequality Platform for Gini coefficients, the World Inequality Database for top-income shares, WHO and World Bank EdStats for health and education spending, the ILO for labor-force indicators, and OECD for the placebo moderator. Every series is cited with its OWID grapher path in the data-availability table (Appendix A2), so any reader can reproduce the panel without proprietary data.

### 4.1 Sample

The treated population is post-1990 democratizers with transitions beginning between 1989 and 1998. Transition is dated from the OWID-hosted V-Dem Regimes of the World classification as the first year of electoral or liberal democracy sustained for at least two consecutive years, cross-checked against the OWID-hosted Boix-Miller-Rosato binary regime series [29, 39]. If the cross-check must draw on the underlying BMR data rather than the OWID-hosted series, that is the paper's single non-OWID input, disclosed here and in the registry. The cohort cap serves the pre-determination logic: for every retained case, the first democratic decade ends before the 2008 crisis and before the 2010-2022 resilience window that H3's dividend must predict. The expected roster is 25 to 35 countries. The roster is fixed deterministically by the dating rule, printed in the registry and in Appendix A1, and no case is added or dropped after estimation begins. Countries with erosion onset within the first twelve years after transition are flagged; the specification with them excluded is pre-committed under Design 6(e) because welfare measured after erosion onset is post-treatment by construction. For comparison, and for the adjudication specification, we also construct the full sample of democracies over 1990-2022, which approximates and extends the Rau-Stokes population, whose sample restriction runs over 1995-2020, to the young democratizers that fell below the democracy threshold [1]. The panel runs 1985-2023, leading the earliest transitions by four years to support event-study pre-trends.

### 4.2 Outcome

The V-Dem Liberal Democracy Index (v2x_libdem, 0-1), hosted on OWID, is the outcome in levels and in five-year differences [28, 40]. A continuous index is essential for graded erosion: the hypothesis concerns how much democratic quality is lost inside formally democratic regimes, and the post-1990 wave contains many episodes of substantial decline that stop short of breakdown. For the event-study designs, erosion onset is defined as the first year of a sustained three-year decline of at least 0.03 in the index, in line with the graded-decline approach of the measurement literature [3]. Robustness to alternative onset codings is pre-committed.

### 4.3 The inequality treatment: pre-fisc by construction

The primary treatment is the WID pre-tax national-income top-10 percent income share, hosted on OWID. It is the theoretically preferred measure for the populism mechanism, since the fear of elite capture in Acemoglu, Egorov, and Sonin is a fear of the very rich [16], and it is the measure type, pre-tax WID shares, that Rau and Stokes use at the top end of their analysis [1]. The secondary treatment is a market-income Gini, the WID pre-tax Gini or the PIP market-income Gini where available on OWID, with the source concept disclosed per country-year. The disposable-income Gini, in which the entanglement problem of Section 2 lives, is demoted to robustness: it appears in the specifications only to document the contrast and to construct the gap.

The gate's first mechanism is measured directly. The market-minus-disposable Gini gap, $g_{it}$, is constructed wherever market and disposable series both exist, with concept tags recording the source combination (expected: WID pre-tax Gini minus PIP disposable Gini, and market-minus-disposable PIP where both exist). Interpolation behavior and per-series coverage flags are printed in the coverage matrix, because the gap is only as good as its two inputs and the design's core identification move cannot rest on silently imputed observations. The gap is entered as a covariate and as a moderator in the mechanism and robustness designs.

The treatment is lagged by three years in the main specification, and distributed lags trace the one-to-six-year profile. The lag structure is fixed before estimation; it implements the three-to-five-year transmission window of H2 and separates the gate from the reverse-causal direction, in which erosion precedes the inequality surge.

### 4.4 The welfare measure and its windows

The gate variable $W_i$ is the sum of domestic general government health expenditure (percent of GDP, WHO series) and government education expenditure (percent of GDP, World Bank EdStats), both hosted on OWID. It is an intentionally non-cash, services measure: public health and public education are the components the broad middle class uses, the components automatic in delivery, and the components an eroding executive must capture to take control of daily life. It excludes pensions and targeted cash by construction.

$W_i$ is set to the average over the earliest available three-year window within years 0 to 8 after transition, and it is time-invariant thereafter. The actual calendar years of the window are documented per country in Appendix A1, because the WHO health series begins near 2000, so early transitions' de facto measurement years are disclosed rather than assumed: a 1991 transition whose earliest available service data begin in 2000 is measured in years 9 to 11, flagged, and retained. The set of early transitions affected by the WHO start date is listed in the coverage matrix. The sensitivity pair is pre-committed: $W$ measured at years T+3 to T+7 and at years T+8 to T+12 is reported alongside the primary earliest-window measure, so any window drift is visible rather than hidden. No country's $W$ is imputed.

The pre-determination logic is the heart of the identification, and it now has three legs. First, $W$ is fixed before typical erosion onset: in the post-1990 cohort, erosion begins on average in the second decade after transition, and the cohort cap plus the early-erosion exclusion rule ensure the measurement window precedes onset in every retained case. Second, $W$ precedes the 2008 crisis and the 2010-2022 resilience window for the entire cohort, so the dividend measure and the resilience outcome are temporally separated. Third, the welfare legacies are inherited rather than chosen: Eastern European democratizers walked into communist-era health and education systems of near-universal coverage, and Latin American and African democratizers into colonial-era public-service skeletons of varying depth. The variance in $W$ is driven by the depth and maintenance of inherited systems through a chaotic first decade, not by long-run welfare design chosen under democratic deliberation.

### 4.5 Placebo moderators and mechanism variables

The universalism contrast of H5 needs a full-sample placebo. The OECD's total social spending (percent of GDP) is pensions-heavy and transfer-dominated, and it is the natural contrast, but it exists only for OECD members, and most of the retained roster, including South Africa, Ukraine, Mongolia, Indonesia, and much of Latin America, would be excluded from an OECD-only placebo. The pre-committed primary placebo is therefore a full-sample transfer measure, the ILO World Social Protection Database or IMF Government Finance Statistics transfers, whichever OWID hosts for the roster; the OECD SOCX analysis is reported as a secondary subsample with its coverage limitation quantified. H5's confirmation does not depend on the OECD-only subsample carrying the claim.

The mechanism variables implement Section 3.2. Stabilization is the gap. Constituency formation is probed with spending composition, the ratio of health-plus-education spending to total social spending, and with usage proxies, public secondary enrollment shares and the V-Dem public-services index, where OWID carries them. Pre-commitment is probed with an automaticity index constructed from entitlement, indexation, and non-discretionary funding features; its data availability is flagged in the coverage matrix, and if the index is unavailable for a substantial share of the roster, the pre-commitment arm is reported as a case-level supplement rather than a panel estimate. The proximate-channel arm uses the V-Dem political polarization index and the ILO educated-youth unemployment rate, the share of 15-24-year-olds with completed education who are unemployed, both hosted on OWID where available.

### 4.6 Controls

The core specifications include log GDP per capita (World Bank, via OWID) and an EU-accession indicator, with country fixed effects absorbing time-invariant regional differences and region-specific trends added in the robustness cells. Commodity dependence, measured as natural-resource rents as a share of GDP, enters the exclusion robustness check. No control is post-treatment with respect to the gate: $W$ is pre-determined by construction, and the treatment is lagged. EU accession is entered both as a level control and, in the trend-controlled specification, as a level plus trend, because the accession process is the most salient welfare-building force in the Eastern European cases and the trend form is the form of the threat.

### 4.7 The divergent trajectories of the cohort

[FIGURE:fig3]

Figure 3 documents the phenomenon the design must explain, with values from the development phase to be re-verified at every series URL in the coverage audit. Among the eleven cases with continuous data, liberal-democratic quality diverged sharply after 2010. Hungary fell from 0.754 in 2005 to 0.335 in 2022. Poland fell from 0.827 in 2010 to 0.417 in 2022. Estonia rose from 0.811 to 0.853 over 2010-2022, and Latvia, Lithuania, and Slovakia held their 2005 levels. Chile consolidated after 2000 and declined mildly after 2015; South Korea fell mid-decade and recovered, ending 2022 at 0.718. South Africa moved from 0.666 in 2010 to 0.610 in 2022, and Bulgaria and Romania fluctuated in an intermediate band. The same wave produced both the sharpest erosion and the most stable resilience in the same region.

Two descriptive facts about inequality discipline the theorizing. First, the eroded countries were not, on the disposable-income Gini, the most unequal in the group. Hungary's Gini fluctuated between 0.27 and 0.35 over 2005-2016, with a trough of 0.270 in 2009; Poland's fell from 0.38 in 2004 to 0.31 in 2016. Second, the resilient countries did not have exceptionally low inequality: Estonia's Gini stayed between 0.31 and 0.35, Latvia's between 0.34 and 0.39 (PIP, via OWID). The cross-sectional correlation between inequality levels and erosion is weak in exactly the way Haggard and Kaufman describe [2]. That fact does not contradict the materialist account, because the Rau-Stokes effect is about movements, not levels, and operates through within-country variation over time [1]. It does mean the theory must be stated in shocks: the gate conditions the transmission of inequality increases, not the standing level of inequality. Section 5 is built for that statement.

The welfare numbers line up with the trajectories' institutional reading. On the development-phase measure, the sum of health and education spending as a share of GDP runs from 10.3 in Lithuania, 9.6 in Hungary, 9.5 in Estonia, 9.0 in Slovakia, 8.9 in Poland, 8.4 in Latvia, 7.5 in Chile, 7.2 in South Africa, to 5.1 in South Korea; Bulgaria and Romania lack usable WHO health series in the early window on OWID (the coverage matrix reports the exact years). Hungary and Poland sit mid-pack on services and eroded at low inequality. If the gate claim is right in its strong form, their erosion must run through channels other than inequality, polarization and elite coalition formation first among them [2, 12]. The welfare-gate hypothesis claims only that the inequality channel is gated by institutions, not that inequality is the only erosion channel. Whether mid-range service spending suffices to gate the inequality channel in Hungary and Poland, against the fiscal reality of pension-dominated welfare states in which the service component stagnated, is an open question that the interaction design, and only the interaction design, can answer. The marginal-effect reporting in Section 6 commits to reporting the inequality effect at welfare values that include the Hungarian and Polish cases, so the crucial cases are inside the support of the test.

### 4.8 Pre-determination and exogeneity probes

The identifying assumption deserves statement in its strongest form, and the probes that would break it are pre-committed. Post-1990 transitions are quasi-exogenous in timing: they cluster in 1989-1991 with the collapse of the Soviet bloc, in 1992-1994 with the Southern African and Central American settlements, and in the late 1990s with the remaining post-communist and Asian cases [39]. At the moment of transition, welfare legacies are inherited. The threat to the assumption is that the first democratic decade itself selects welfare depth: governments that consolidated well also maintained services. The design confronts this threat with five pre-committed probes.

First, balancing regressions: $W$ is regressed on first-decade inequality changes and on fiscal-collapse indicators, inflation and output collapse, to show that $W$ is not itself a product of the inequality dynamics the gate is meant to condition. Second, an instrumented version of Design 1: $W$ is instrumented with legacy variables, communist-era schooling enrollment and colonial-era public-service coverage, with 2SLS estimates reported; the roster feasibility of each instrument is documented in the registry, and any shortfall is reported rather than papered over. Third, the within-Eastern-Europe estimate holds the communist legacy constant and varies only the depth of inherited health and education systems, where first-decade maintenance was driven by fiscal collapse and stabilization programs rather than democratic politics. Fourth, the placebo moderator splits the measure: if the protective variable were really democratic-quality selection, the pension-heavy total-spending measure would gate as well, and H5 predicts it does not. Fifth, the early-erosion exclusion rule removes the cases for which $W$ is post-treatment by construction. Each probe addresses a specific version of the selection story, and Section 6 states what each failure would mean.

The coverage matrix closes the data section. Appendix A2 tabulates, for every roster country, every series, and every window: availability, first and last observed year, observation count, interpolation flag, and the OWID grapher URL. The effective estimation sample for each of the six designs is printed from the matrix before estimation. If listwise deletion drops an effective sample below 25 countries, the minimum-detectable-effect analysis of Section 5.7 is recalibrated to the realized sample and reported, no imputation fills the gaps, and the confirmation criteria are interpreted at the realized power. The matrix is the answer to the coverage question a reviewer must ask of a 25-to-35-country design: every cell is either present with a URL or absent with a reason.
## 5. Research Design

All estimation is implemented in Python (linearmodels and statsmodels), with the staggered event studies estimated by Sun-Abraham via pyfixest and by Callaway-Sant'Anna via the R implementation through rpy2 or a documented manual implementation [30, 31]. Standard errors are clustered at the country level; the interaction tests use wild cluster bootstrap inference, given the modest number of clusters. The full code and the constructed panel are released with the registry deposit, so every number in the companion results paper is generated by the deposited code from the deposited data. Figure 4 summarizes the identification logic.

[FIGURE:fig4]

### 5.1 Design 1: the gate test

The core specification is a two-way fixed-effects regression with welfare-specific trends:

$$\text{LibDem}_{it} = \alpha_i + \delta_t + \beta_1 m_{i,t-3} + \beta_2 \left(m_{i,t-3} \times W_i\right) + \gamma_1 W_i t + \gamma_2 W_i t^2 + X_{it}'\theta + \varepsilon_{it},$$

where $i$ indexes countries, $t$ years, $\alpha_i$ and $\delta_t$ are country and year fixed effects, $m_{i,t-3}$ is the lagged pre-fisc inequality treatment, and $W_i$ is the pre-determined welfare measure, absorbed by the country fixed effects in its own right with the interaction identified. The welfare-specific trends $W_i t$ and $W_i t^2$ are the identification change this registration makes relative to the designs reviewed in Section 2: any factor correlated with $W$ and with democratic trajectories, EU accession, fiscal capacity, geopolitical alignment, is absorbed in the trend terms, and the gate is identified off deviations from welfare-specific trends. The gate hypothesis is $\beta_2 > 0$, large enough that the marginal effect $\beta_1 + \beta_2 W$ is near zero or positive in the high-welfare arm and strongly negative in the thin-welfare arm. We report the marginal effect at the 10th, 25th, 50th, 75th, and 90th percentiles of the welfare distribution, with wild cluster bootstrap confidence intervals, and the linear and quadratic functional forms pre-committed in Section 3.1. Because two-way fixed-effects estimators with differential timing can be biased under heterogeneous effects, we also estimate the interacted specification on five-year differences of the outcome and report Goodman-Bacon decompositions where timing variation is involved [41].

The critical control variant is the gap-controlled specification, which in the same equation adds $g_{i,t-3}$ and $g_{i,t-3} \times W_i$. Its reading is fixed in advance. If $\beta_2$ collapses toward zero once the gap and its interaction are included, the gate is fiscal filtering: the interaction was the first mechanism measured, and no behavioral residue exists. If $\beta_2$ survives, a behavioral residue exists and is attributed to constituency formation and pre-commitment, which Designs 5 and 6 then discriminate further.

### 5.2 Design 2: the adjudication specification

To make the reconciliation claim directly, we estimate the baseline inequality main effect without any interaction, on the full democracy sample and on the young-democracy sample, and then introduce the interaction. The protocol commits to reading the two specifications jointly. A weak or insignificant main effect with a strong and significant interaction is the pattern that reconciles Rau and Stokes with Haggard and Kaufman [1, 2], because it says the average effect hides institutional heterogeneity rather than being absent. A strong unconditional main effect that survives the interaction is instead evidence for the unconditional materialist account. A null everywhere is evidence for the purely coalitional account. The three-way reading is pre-committed before estimation, so the adjudication cannot be renegotiated after the results are in.

### 5.3 Design 3: erosion-onset event studies and sequencing

We stack erosion onsets among post-1990 democratizers and estimate dynamic coefficients relative to onset, separately for the high-welfare and thin-welfare arms defined by a median split of $W$. The estimators are Callaway-Sant'Anna and Sun-Abraham, chosen because onsets are staggered across the cohort and treatment effects are plausibly heterogeneous [30, 31]; the Goodman-Bacon decomposition documents the composition of any two-way fixed-effects benchmark [41]. Pre-trend tests are pre-committed and reported for both arms. The event-study coefficients trace the Liberal Democracy Index, market inequality, and public-services spending in the eight years before and after onset. The confirmation pattern for H2: in the thin-welfare arm, inequality and service retrenchment rise before the index declines; in the high-welfare arm, no such pre-onset movement appears. The lead-lag structure is the primary defense against reverse causality. If erosion caused welfare decline, services would fall only after onset; the hypothesis requires service decline to lead erosion in the thin-welfare arm and to be absent in the high-welfare arm. This also separates the gate's direction from the outcome-side literature that documents welfare transformed under backsliding [17, 18, 19, 20].

### 5.4 Design 4: the democratization event study and the dividend

We align countries at the transition year $T$ and estimate the dynamic path of the top-10 percent income share, public services, and education over the two decades after transition, separately by pre-determined welfare legacy, above or below the sample median. The dividend window is fixed at years 0 to 7 after transition, so the dividend precedes the 2008 crisis and the 2010-2022 resilience window for every retained case. The confirmation pattern for H3: the top-10 percent share declines in years 0 to 7 only in high-welfare-legacy countries, and the size of that first-decade decline predicts the 2010-2022 change in the Liberal Democracy Index, in a country-level regression that reports the dividend-resilience slope with its confidence interval. This extends the democratic-dividend result [24] by conditioning its inequality leg on welfare institutions and by connecting the dividend to subsequent resilience, with the dividend measured before the resilience outcome.

### 5.5 Design 5: mechanism arms

(a) Stabilization: the gap-controlled variant of Design 1, whose reading is fixed in Section 5.1. (b) Constituency formation: the interaction is re-estimated with spending composition, the health-plus-education share of total social spending, and usage proxies entered as additional moderators and controls; attenuation is the pattern that assigns work to the constituency channel. (c) Pre-commitment: the automaticity index is interacted with the treatment in the same design; the gate should be stronger where services are automatic. (d) Proximate channels: the inequality-by-thin-welfare interaction is estimated on the V-Dem polarization index, and a triple interaction of inequality, thin welfare, and educated-youth unemployment tests whether the gate tightens where education expands without absorption [36]. Arms (a) through (c) are the mechanism discrimination the theory requires; arm (d) is a mechanism report in the proximate channel already occupied by the rival account, and it is interpreted with that status, as Section 3.4 pre-commits.

### 5.6 Design 6: robustness

Seven cells are pre-committed, and every one is reported, including the ones that fail. (a) Alternative treatments: the market-income Gini for the top-10 percent share, and the disposable Gini entered only to document the contrast that motivates the design. (b) Alternative welfare measures: health and education entered separately; the sum entered continuously and as an above/below-median split. (c) Population weights. (d) Exclusion of the commodity-boom countries, identified by natural-resource rents above a threshold. (e) The within-Eastern-Europe estimate, holding the communist legacy constant; the early-erosion exclusion, dropping or recoding cases with erosion onset within the first twelve years; and the EU-accession trend control. (f) Wild cluster bootstrap confidence intervals for the interaction and the marginal effects. (g) Placebo moderators: total social spending from the full-sample transfer measure, the ILO World Social Protection Database or IMF Government Finance Statistics series, and the OECD SOCX measure on its OECD subsample; plus a placebo interaction of $W$ with a within-country variable unrelated to inequality, population age structure, which the gate account predicts is null. The placebo cells are the falsification of the H5 contrast: a gate reproduced by pensions or by targeted or chauvinist transfers disconfirms the universalism claim.

### 5.7 Power, minimum detectable effects, and the registry

Power for an interaction test in a panel of 25 to 35 countries with serially correlated outcomes is the binding constraint, and the criteria in Section 6 are calibrated to it. Before estimation, a simulation-based minimum-detectable-effect analysis is run on the actual panel structure: a two-way fixed-effects DGP with the realized country roster, the realized $W$ distribution, and the realized treatment moments, under serial correlation of the outcome at rho 0.7, 0.8, and 0.9 and effective N of 25, 30, and 35. The analysis reports the minimum detectable $\beta_2$ and the minimum detectable marginal effect at the 10th percentile of $W$, at 80 percent power, and the report is deposited with the registry. Two consequences follow and are accepted in advance. The study is powered to detect a large conditional effect, which is what the theory predicts: the Section 3 sketch implies near-complete transmission where welfare is thin and near-zero transmission where it is thick. And the confirmation criteria are stated for effects of that size; a weak gate would go undetected, and the paper will say so rather than claim a null.

The registry closes the design. The protocol, the roster, the coverage matrix, the MDES analysis, and the deposited code are timestamped at OSF before any estimation. The primary specification is Design 1 with the pre-fisc treatment, the earliest-window $W$, and welfare-specific trends. The decision rule, fixed in advance: the gate holds if the interaction is significant at p < 0.05 and the marginal-effect pattern is confirmed in the primary specification and in at least five of the seven robustness cells, with failures reported and interpreted. No specification is added after estimation; no specification is dropped; the deposited code generates every number in the companion paper.
## 6. Expected Results and Falsification Criteria

The protocol commits ex ante to the following inference rules, so that the test can adjudicate between the accounts. Figure 5 graphs the pre-registered prediction for the gate's marginal effect against the two alternative accounts.

[FIGURE:fig5]

**Confirmation** of the welfare-gate hypothesis requires five conditions. (a) A significant positive interaction between lagged pre-fisc inequality and pre-determined welfare strength on liberal-democracy trajectories, under welfare-specific trend controls, with the within-country inequality effect near zero or positive in the high-welfare arm and strongly negative in the thin-welfare arm: the marginal effect at the 10th and 25th percentiles of $W$ is negative with a confidence interval excluding zero, and the marginal effect at the 90th percentile is not significantly negative. The gate holds if this pattern appears in the primary specification and in at least five of the seven robustness cells, with failures reported and interpreted. (b) Sequencing: market-inequality surges and public-service retrenchment lead liberal-democracy declines by three to five years in thin-welfare countries, no anticipatory service decline precedes erosion onset in the high-welfare arm, and pre-trend tests pass in both arms. (c) The welfare-dependent dividend: the top-10 percent income share declines in years 0 to 7 after democratization only in high-welfare-legacy countries, and the size of that first-decade decline predicts the 2010-2022 change in the Liberal Democracy Index. (d) At least one discriminating mechanism result from Design 5, with the readings fixed in Section 5.1 and stated again here: the interaction collapses when the gap and its interaction are controlled, and stabilization is the mechanism; or the interaction attenuates with composition and usage controls, and constituency formation is the mechanism; or the interaction is concentrated in automatic programs and absent for discretionary late-bought transfers, and pre-commitment is the mechanism. (e) The universalism contrast: public services gate; the full-sample transfer placebo and the OECD total social spending measure do not, in their respective samples.

**Disconfirmation** is equally sharp, and each outcome has a clear interpretation in the literature. A homogeneous inequality effect across welfare arms, or an insignificant or wrong-signed interaction in the primary specification, falsifies the gate and favors the unconditional materialist account [1, 8]. An interaction that collapses once welfare-specific trends are added falsifies the gate in favor of a selection reading in which a third factor drives both welfare maintenance and democratic resilience. Reversed sequencing, with service decline following erosion onset, favors the outcome-side transformation literature [17, 18, 19, 20] over the gate. A gate reproduced by the pension or targeted-cash placebo disconfirms the universalism claim, H5, even if H1 holds. A dividend that appears in thin-welfare countries disconfirms the welfare-dependent-dividend claim, H3. Every one of these outcomes adjudicates among the accounts, so the study is a genuine three-way test and a null result is itself a contribution: it would mean the unconditional materialist or the purely coalitional account survives the institutional test.

Two interpretive commitments deserve emphasis because they are the ones a design can quietly reverse. First, the arithmetic-only reading is pre-committed. Under the arithmetic-only account, in which automatic stabilization filters inequality but institutions change no behavior, the gate interaction in the gap-controlled specification disappears completely, and the residual market effect is homogeneous in $W$. Under the behavioral account, a residual interaction survives. The results are read through that dichotomy, and the two mechanisms that survive the gap control, constituency formation and pre-commitment, are then assigned by the Design 5 attenuation patterns. Second, the marginal-effect reporting standard: the gate claim lives or dies on the inequality marginal effect at the welfare-distribution percentiles, not on the interaction coefficient alone, because a significant interaction with a negative marginal effect everywhere would not constitute a gate. The percentile plot and the Hungarian and Polish values inside the support are part of the report, not an afterthought.

## 7. Discussion

The welfare-gate hypothesis is offered as a resolution to a dispute that has been stuck because its two protagonists estimate different objects, and one of them measures its treatment through the very institutions the dispute is about. The value of the design lies in what each possible outcome would teach. We discuss three central readings before the data arrive.

**Reconciling the two accounts.** If H1 and H2 hold, the Rau-Stokes inequality effect [1] and the Haggard-Kaufman economic skepticism [2] are not in tension. The inequality effect in the global sample is carried by the thin-welfare democracies: the post-communist laggards, the Latin American service skeletons, the Southern African cases where public services reach only part of the population. In the high-welfare arm, inequality rises without erosion, which is why close comparison of resilient cases finds no economic story. The case-based account studied mostly the backsliders, Hungary, Poland, Turkey, and the statistical account studied mostly the pooled average. Both were right about their effective samples and wrong about the population. The gate also disciplines the level-versus-shock distinction that the descriptive data force on us: Hungary and Poland eroded at low inequality, so the inequality channel cannot be their whole story; the gate claim is that where inequality shocks did occur, their transmission depended on institutions. That is a narrower claim than the materialist account makes, and the design is built to test exactly that claim.

The pre-fisc correction changes what a confirming result would mean for the materialist account itself. If the gate survives on the pre-tax top-10 percent share and on the market Gini, the inequality-erosion link is real but institutionally conditioned, which is the reconciliation. If the gate appears on the disposable Gini and dissolves on the pre-fisc measures, the Rau-Stokes main effect is partly fiscal filtering after all: the disposable Gini fell in high-welfare countries partly because their fiscal systems compressed it, and the "protective" welfare state and the "compressed" treatment are the same object measured twice. The design's contrast specifications are built so the results can say which reading holds.

**The democratic dividend, conditioned.** The most consequential extension is to the democratic-dividend literature. Acemoglu, Naidu, Restrepo, and Robinson established that democratization raises taxation and schooling, and found no robust average inequality reduction, with imprecise estimates and heterogeneity they could not fully explain [24]. The welfare-gate account supplies a candidate conditioner: the inequality-reduction leg of the dividend materializes only where universal service institutions are strong enough to convert fiscal expansion into distributional change. In thin-welfare democratizers, higher taxation without service delivery produces neither redistribution nor a middle-class constituency attached to public provision. The first-decade dividend, or its absence, is then the mechanism that connects democratization to its own fate: countries whose first democratic decade did not deliver the visible, universal dividend entered the crisis years with no welfare buffer and no service constituency, precisely the configuration that H1 predicts erodes under inequality pressure. If H3 and H4 hold, the dividend literature and the erosion literature are one literature: the dividend is the resilience mechanism, and its failure is the erosion mechanism. This also reframes the education-and-democracy null [35]: education produces democratic resilience through absorption into middle-class employment and enrollment in public services, not through values socialization alone. Where education expands without absorption, the Campante-Chor mismatch [36] operates, and the educated young become an erosion resource rather than a democratic one. The cleavage-structure results of Gethin, Martinez-Toledano, and Piketty [38] and the redistributive politics of education in Ansell [37] are the microfoundations of that channel. We repeat the caution of Section 6: all of this is conditional on the design confirming, and the design is registered precisely so that a reader can tell the difference between a confirming and a disconfirming pattern without trusting the authors' later description of what they intended.

**The universalism contrast and the policy reading.** The sharpest claim in the paper is H5: total social spending and late-bought generosity do not gate. If H5 holds, the policy implication is not spend more on welfare but build universal service institutions early. For the post-1990 cohort and for any future democratization wave, the testable prescription is that the first democratic decade is the window in which universal health and education systems must be constructed, because legitimacy and constituency are built by the institutions that exist when the first crisis arrives. Welfare effort purchased later, targeted cash, chauvinist family allowances, functions as pacification [19] and as an instrument of the eroding incumbent [17, 18, 20]. The distinction between universal services and total social spending is the distinction between institutions that create their own defenders [13, 14, 15, 23] and expenditures that buy quiescence.

South Africa is the sharpest challenge to the gate's thin-welfare arm. It combines the cohort's highest inequality, a Gini near 0.65 at its 2005 peak and still 0.61 in 2010, with only modest liberal-democratic decline, from 0.666 in 2010 to 0.610 in 2022. A purely materialist account would predict more erosion; the gate account reads the pattern as delayed or partial transmission, with the state-capture scandals of the 2010s as the first installment. The timing tests in Design 3 are what distinguish these readings, and the protocol commits to reporting South Africa's residual explicitly.

## 8. Limitations

Five limitations are intrinsic to the design, and we state them as such rather than as future work.

**Small N and statistical power.** The treated sample is 25 to 35 countries, and the interaction is a difference-in-differences of a difference-in-differences: the effective variation is the within-country association between inequality and liberal democracy, compared across welfare arms. Power for interaction tests is low in samples of this size, and the clustered standard errors rest on a modest number of clusters. The pre-committed MDES analysis defines what the design can detect before estimation, and the confirmation criteria are stated for the large conditional effects the theory predicts. The study will not detect a weak gate, and the results paper will say so if the confidence intervals cannot exclude one.

**The welfare measure is a proxy.** Public health and education spending as a share of GDP measures fiscal effort, not universality, not quality, and not usage by the middle class. Two countries with identical spending shares can differ in whether public hospitals serve the well-off or only the poor, and the mechanism in H1 is about usage. The proxy bias is conservative: measurement error in the gate variable attenuates the interaction and biases against confirmation. Composition and usage controls partially discipline the proxy, but the ideal test would require usage data that OWID panels do not fully carry, and the coverage matrix will say exactly how far the usage proxies reach.

**Identification of the gate.** The welfare measure is pre-determined relative to erosion onset, but it is not randomly assigned. The first democratic decade is itself a period of democratic politics, and governments that consolidated well also maintained services. The balancing regressions, the legacy-instrument 2SLS, the within-Eastern-Europe estimate, the placebo moderator, and the early-erosion exclusion each address a specific version of this threat, and the welfare-specific trends absorb the shared-trend version, but none eliminates the possibility that a third factor, state capacity, geography, or geopolitical alignment, drives both welfare maintenance and democratic resilience. EU accession is the most salient such factor for the Eastern European cases, and it was itself a welfare-building force in the first decade, which means the gate and the accession channel are partially entangled by construction. The time-invariant nature of the moderator means the cross-sectional weight in the interaction is correlational by design; the identification claims are about the within-country inequality dynamics that the trends and lags discipline.

**Measurement of the outcome and the treatment.** The Liberal Democracy Index is expert-coded, and its inter-temporal comparability is contested [3]. The Gini coefficient's cross-country comparability is limited by differing underlying surveys and income concepts; PIP and WID harmonization, while the best available, does not remove the issue. Both biases are plausibly classical in this design, attenuating main effects and interactions alike, but the threat to the sequencing tests is asymmetric: if erosion onset is misdated, the lead-lag structure in Design 3 shifts, and the confirmation pattern for H2 could be manufactured by measurement timing. We address this with the three-year sustained-decline coding rule, robustness to alternative onset codings, and the requirement that the sequencing pattern differ across welfare arms, which a pure measurement artifact would not produce.

**The placebo subsample problem.** The sharpest contrast, H5, requires a full-sample placebo, and the full-sample transfer measure is the pre-committed answer. The OECD SOCX measure exists only for OECD members, and an H5 test run only on that subsample could not carry the paper's strongest claim; the OECD-only analysis is reported as a secondary subsample with its coverage limitation quantified. If the ILO or IMF full-sample series proves unavailable on OWID for a substantial share of the roster, that finding is itself a registered limitation: the universalism contrast would then rely on the composition contrast within the health-plus-education measure, health versus education entered separately, and on the within-country contrast between discretionary and automatic spending, and the paper would say so.

## 9. Conclusion

The post-1990 democratizers are the population on which the dispute about democratic erosion should be adjudicated, and they are the population the global statistical literature has excluded. This paper has argued that the adjudicating variable is the welfare state, specifically the universal service state built in the first democratic decade, and that the field's flagship treatment, disposable-income inequality, is compressed by the very institutions the gate hypothesis implicates. The hypothesis is precise: market-inequality surges erode young democracies only where welfare institutions are too thin to absorb them, the fiscal filter is measured directly as the market-minus-disposable gap, and the inequality-reduction leg of the democratic dividend materializes only behind the gate. The design is fixed: an OWID-only panel, a pre-determined welfare measure with documented windows, a pre-fisc treatment, welfare-specific trend controls, staggered event studies with estimators built for differential timing, exogeneity probes, a fixed roster with a coverage matrix, a power analysis, and a timestamped registry. The descriptive data show why the adjudication matters: the same wave produced both the sharpest erosion and the most stable resilience, and the eroded countries were not the most unequal. If the evidence confirms the gate, the reconciliation of the materialist and coalitional accounts is institutional: inequality matters, but its effect is conditional on institutions that half the post-1990 wave never built, and part of the materialist account's pooled effect is the fiscal filtering of its own treatment. If it disconfirms, the unconditional accounts stand, and the adjudication is still progress. The results paper will report against the criteria fixed here, and the registry entry will make the difference between the two visible to any reader.

## Appendix

**A1. Candidate roster and transition years.** The roster is fixed deterministically from the OWID-hosted V-Dem Regimes of the World series, cross-checked against Boix-Miller-Rosato, and is printed in full, country by country with transition year and dating source, in the registry and in the supplementary materials of the companion results paper. No case is added or dropped after estimation begins. The eleven cases of Figure 3, Bulgaria, Chile, Estonia, Hungary, Latvia, Lithuania, Poland, Romania, Slovakia, South Africa, and South Korea, are listed here as the illustrative subset; the full roster is produced by the dating rule of Section 4.1, and its coverage appears in Appendix A2.

**A2. Data-availability and coverage matrix.** Country by variable by window: availability, first and last observed year, observation count, interpolation flag, OWID grapher URL.

**A3. Minimum-detectable-effect analysis.** Simulation results on the realized panel under rho 0.7, 0.8, 0.9 and effective N 25, 30, 35.

**A4. Registry deposit checklist.** Protocol text, roster, coverage matrix, MDES report, code, panel construction script, decision rules, dated OSF deposit.

## References

[1] Rau, Eli G., and Susan Stokes. 2025. "Income Inequality and the Erosion of Democracy in the Twenty-First Century." *Proceedings of the National Academy of Sciences* 122(1): e2422543121. doi:10.1073/pnas.2422543121.

[2] Haggard, Stephan, and Robert R. Kaufman. 2021. *Backsliding: Democratic Regress in the Contemporary World*. Cambridge: Cambridge University Press. doi:10.1017/9781108957809.

[3] Waldner, David, and Ellen Lust. 2018. "Unwelcome Change: Coming to Terms with Democratic Backsliding." *Annual Review of Political Science* 21: 93-113. doi:10.1146/annurev-polisci-050517-114628.

[4] Bermeo, Nancy. 2016. "On Democratic Backsliding." *Journal of Democracy* 27(1): 5-19. doi:10.1353/jod.2016.0012.

[5] Levitsky, Steven, and Daniel Ziblatt. 2018. *How Democracies Die*. New York: Crown.

[6] Lührmann, Anna, and Staffan I. Lindberg. 2019. "A Third Wave of Autocratization Is Here: What Is New about It?" *Democratization* 26(7): 1095-1113. doi:10.1080/13510347.2019.1582029.

[7] Grumbach, Jacob M. 2023. "Laboratories of Democratic Backsliding." *American Political Science Review* 117(3): 967-984. doi:10.1017/S0003055422000934.

[8] Houle, Christian. 2009. "Inequality and Democracy: Why Inequality Harms Consolidation but Does Not Affect Democratization." *World Politics* 61(4): 589-622. doi:10.1017/S0043887109990074.

[9] Acemoglu, Daron, and James A. Robinson. 2006. *Economic Origins of Dictatorship and Democracy*. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511510809.

[10] Boix, Carles. 2003. *Democracy and Redistribution*. Cambridge: Cambridge University Press. doi:10.1017/CBO9780511804960.

[11] Ansell, Ben W., and David J. Samuels. 2014. *Inequality and Democratization: An Elite-Competition Approach*. New York: Cambridge University Press. doi:10.1017/CBO9780511843686.

[12] Svolik, Milan W. 2019. "Polarization versus Democracy." *Journal of Democracy* 30(3): 20-32. doi:10.1353/jod.2019.0039.

[13] Pierson, Paul. 1993. "When Effect Becomes Cause: Policy Feedback and Political Change." *World Politics* 45(4): 595-628. doi:10.2307/2950710.

[14] Soss, Joe, and Sanford F. Schram. 2007. "A Public Transformed? Welfare Reform as Policy Feedback." *American Political Science Review* 101(1): 111-127. doi:10.1017/S0003055407070049.

[15] Rothstein, Bo, and Eric M. Uslaner. 2005. "All for All: Equality, Corruption, and Social Trust." *World Politics* 58(1): 41-72. doi:10.1353/wp.2006.0022.

[16] Acemoglu, Daron, Georgy Egorov, and Konstantin Sonin. 2013. "A Political Theory of Populism." *The Quarterly Journal of Economics* 128(2): 771-805. doi:10.1093/qje/qjs077.

[17] Szikra, Dorottya, and Kerem Gabriel Öktem. 2023. "An Illiberal Welfare State Emerging? Welfare Efforts and Trajectories under Democratic Backsliding in Hungary and Turkey." *Journal of European Social Policy* 33(2): 201-215. doi:10.1177/09589287221141365.

[18] Lendvai-Bainton, Noemi, and Dorota Szelewa. 2021. "Governing New Authoritarianism: Populism, Nationalism and Radical Welfare Reforms in Hungary and Poland." *Social Policy & Administration* 55(4): 559-572. doi:10.1111/spol.12642.

[19] Vanhuysse, Pieter. 2006. *Divide and Pacify: Strategic Social Policies and Political Protests in Post-Communist Democracies*. Budapest: Central European University Press.

[20] Benczes, István, and Joanna Orzechowska-Wacławska. 2024. "Governing the Economy under Populist Rule: The Cases of Hungary and Poland." *Problems of Post-Communism* 71(4): 341-355. doi:10.1080/10758216.2023.2301085.

[21] Ennser-Jedenastik, Laurenz. 2018. "Welfare Chauvinism in Populist Radical Right Platforms: The Role of Redistributive Justice Principles." *Social Policy & Administration* 52(1): 293-314. doi:10.1111/spol.12325.

[22] Esping-Andersen, Gøsta. 1990. *The Three Worlds of Welfare Capitalism*. Princeton, NJ: Princeton University Press.

[23] Korpi, Walter, and Joakim Palme. 1998. "The Paradox of Redistribution and Strategies of Equality: Welfare State Institutions, Inequality, and Poverty in the Western Countries." *American Sociological Review* 63(5): 661-687. doi:10.2307/2657333.

[24] Acemoglu, Daron, Suresh Naidu, Pascual Restrepo, and James A. Robinson. 2015. "Democracy, Redistribution, and Inequality." In *Handbook of Income Distribution*, vol. 2, eds. Anthony B. Atkinson and Francois Bourguignon, 1885-1966. Amsterdam: Elsevier. doi:10.1016/B978-0-444-59429-7.00022-4.

[25] Svolik, Milan W. 2015. "Which Democracies Will Last? Coups, Incumbent Takeovers, and the Dynamic of Democratic Consolidation." *British Journal of Political Science* 45(4): 715-738. doi:10.1017/S0007123413000550.

[26] Huber, Evelyne, and John D. Stephens. 2001. *Development and Crisis of the Welfare State: Parties and Policies in Global Markets*. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226356495.001.0001.

[27] Huber, Evelyne, and John D. Stephens. 2012. *Democracy and the Left: Social Policy and Inequality in Latin America*. Chicago: University of Chicago Press. doi:10.7208/chicago/9780226356556.001.0001.

[28] Our World in Data. 2025. *Our World in Data* [online database]. https://ourworldindata.org.

[29] Boix, Carles, Michael Miller, and Sebastian Rosato. 2013. "A Complete Data Set of Political Regimes, 1800-2007." *Comparative Political Studies* 46(12): 1523-1554. doi:10.1177/0010414012463905.

[30] Callaway, Brantly, and Pedro H. C. Sant'Anna. 2021. "Difference-in-Differences with Multiple Time Periods." *Journal of Econometrics* 225(2): 200-230. doi:10.1016/j.jeconom.2020.12.001.

[31] Sun, Liyang, and Sarah Abraham. 2021. "Estimating Dynamic Treatment Effects in Event Studies with Heterogeneous Treatment Effects." *Journal of Econometrics* 225(2): 175-199. doi:10.1016/j.jeconom.2020.09.006.

[32] Haggard, Stephan, and Robert R. Kaufman. 2012. "Inequality and Regime Change: Democratic Transitions and the Stability of Democratic Rule." *American Political Science Review* 106(3): 495-516. doi:10.1017/S0003055412000287.

[33] Haggard, Stephan, and Robert R. Kaufman. 2016. *Dictators and Democrats: Masses, Elites, and Regime Change*. Princeton, NJ: Princeton University Press.

[34] Lührmann, Anna. 2021. "Disrupting the Autocratization Sequence: Towards Democratic Resilience." *Democratization* 28(5): 1017-1039. doi:10.1080/13510347.2021.1928080.

[35] Acemoglu, Daron, Simon Johnson, James A. Robinson, and Pierre Yared. 2005. "From Education to Democracy?" *American Economic Review* 95(2): 44-49. doi:10.1257/000282805774669916.

[36] Campante, Filipe R., and Davin Chor. 2012. "Why Was the Arab World Poised for Revolution? Schooling, Economic Opportunities, and the Arab Spring." *Journal of Economic Perspectives* 26(2): 167-188. doi:10.1257/jep.26.2.167.

[37] Ansell, Ben W. 2010. *From the Ballot to the Blackboard: The Redistributive Political Economy of Education*. Cambridge: Cambridge University Press.

[38] Gethin, Amory, Clara Martinez-Toledano, and Thomas Piketty. 2022. "Brahmin Left versus Merchant Right: Changing Political Cleavages in 21 Western Democracies, 1948-2020." *The Quarterly Journal of Economics* 137(1): 1-48. doi:10.1093/qje/qjab036.

[39] Lührmann, Anna, Marcus Tannenberg, and Staffan I. Lindberg. 2018. "Regimes of the World (RoW): Opening New Avenues for the Comparative Study of Political Regimes." *Politics and Governance* 6(1): 60-77. doi:10.17645/pag.v6i1.1214.

[40] Coppedge, Michael, John Gerring, Carl Henrik Knutsen, Staffan I. Lindberg, et al. 2024. *V-Dem [Country-Year/Country-Date] Dataset v14*. Varieties of Democracy (V-Dem) Project. https://v-dem.net.

[41] Goodman-Bacon, Andrew. 2021. "Difference-in-Differences with Variation in Treatment Timing: History, Theory, and Application." *Journal of Econometrics* 225(2): 254-277. doi:10.1016/j.jeconom.2021.03.014.

</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (evidence) No model has been estimated, and the paper's own target - APSR, World Politics, Journal of Democracy - does not publish design-only manuscripts. The paper now states this is a pre-registered design written for venues that publish registered designs, which is honest, but the submission goal stated for this project is these three results venues, and at those venues a protocol with zero estimates cannot be accepted regardless of design quality. Every headline claim (H1-H5, the reconciliation, the welfare-dependent dividend) remains a prediction; the abstract's 'the test can adjudicate' is a promise about a future test.
  Action: Execute the six designs now on the realized OWID roster (at minimum: Design 1 primary spec and its gap-controlled variant, Design 2 adjudication, Design 4 dividend event study, and Design 3 event studies around erosion onsets) and resubmit as a results paper reporting against the Section 6 criteria, with the registry entry and code deposit as appendices. If a design-only submission is intended instead, retarget a venue that publishes pre-analysis plans and say so in the cover letter; do not submit this protocol to APSR/WP/JOD as-is. Expected score impact: the single largest - this change alone moves the paper from 'protocol' to 'results paper' and unlocks the 7-9 range if the findings are interpretable under the pre-committed rules.
- [MAJOR] (rigor) The pre-registration is asserted but not evidenced: there is no OSF registry ID, no deposit date, and the abstract itself says the ID 'is fixed at the moment of deposit' - i.e., the deposit is future. 'Fixed before estimation' and 'timestamped at OSF before any estimation' are claims the reader cannot verify, and because no estimation has occurred, the ex-ante status of the decision rules is untestable in principle. This was flagged in the previous round and remains substantively unaddressed.
  Action: Deposit the protocol, roster, coverage matrix, MDES report, and code on OSF now (before any further estimation-related work), and print the registry URL/ID and deposit timestamp in the abstract and Section 5.7. Fill out the A4 registry checklist as an actual artifact, not a stub. If the deposit has already happened, cite it; the paper currently reads as if it has not. Expected score impact: high - this converts the central epistemic claim of the paper from assertion to verifiable fact and is required for any design venue to take the pre-commitments seriously.
- [MAJOR] (evidence) The paper's core data-infrastructure deliverables - the fixed roster (A1), the coverage matrix (A2), and the MDES analysis (A3) - are stubs. Appendix A1 lists only 11 illustrative cases; the full roster produced by the 'deterministic' dating rule is not printed anywhere in the paper; A2 and A3 are one-line placeholders. Consequently the design's central feasibility claims cannot be checked: the asserted N of 25-35, the availability of the WID pre-tax top-10% share on OWID for a roster including Mongolia, Ukraine, South Africa, and Indonesia, the existence of any market-income Gini series on OWID (I could not confirm one; OWID's Ginis are PIP/WB disposable and WID pre-tax), the availability of a full-sample ILO/IMF transfer placebo (the paper hedges 'whichever OWID hosts'), and the MDES numbers that the Section 6 confirmation criteria are supposed to be calibrated to. Relatedly, small-N designs of this type should pre-commit leave-one-out influence analysis (e.g., Russia, Ukraine, South Africa) since single cases can dominate the interaction.
  Action: Before resubmission, print the full deterministic roster with transition years and dating source; produce the coverage matrix (country x series x window with first/last year, count, interpolation flag, OWID URL) as an appendix table, not a stub; run and print the MDES tables for the realized panel under rho 0.7-0.9 and N 25/30/35; state the effective estimation sample per design; confirm or refute the OWID existence of the market-income Gini and the transfer placebo now rather than at estimation time; and pre-commit a leave-one-out analysis (dropping each of ~5 influential cases) in Design 6. Expected score impact: high - feasibility is the load-bearing premise of any registered design, and reviewers currently cannot verify any of it.
- [MAJOR] (methodology) The 'first democratic decade' measurement window still drifts for the core cohort. Because the WHO health series begins near 2000 and the education series (World Bank/UNESCO on OWID) is available earlier, the earliest three-year window in years 0-8 in which BOTH components of W exist is 2000-2002 for essentially all 1989-1993 transitions - i.e., years 9-11, the second decade, the EU-accession-negotiation period. The paper flags and retains these cases and reports the T+3..T+7 / T+8..T+12 sensitivity pair, which makes the drift visible; but visibility is not correction, and the primary W measure for the majority of the roster is not 'the first democratic decade' as the theory repeatedly claims. A second consequence is compositional: for early transitions W is effectively education(early 1990s) plus health(~2000), so the two components are measured at different calendar periods and the relative weights of health versus education in W vary by case in a way that correlates with transition timing.
  Action: Pre-commit a second primary-adjacent measure, education-only W over years 0-8, for early transitions (education is the component available in the actual first decade), and report the health+education sum as co-primary with component-specific windows and a concept-composition flag. Reframe the theory's language from 'built in the first democratic decade' to 'the pre-crisis, pre-accession window' wherever the data actually force years 9-11, and pre-commit which framing governs interpretation if windows drift. Expected score impact: medium-high - the pre-determination argument (W inherited, W precedes the outcome) is the identification's foundation, and a primary measure admitted to be measured in the wrong decade undercuts it.
- [MAJOR] (methodology) H3's dividend prediction is likely mis-specified against the data as it will actually arrive. WID pre-tax top-10% shares for the post-communist high-welfare cases - Poland, Hungary, the Baltics, Bulgaria, Romania - ROSE during the first 7 years after transition (1989-1996 etc.) as liberalization disequalized, regardless of inherited welfare depth; the dividend window years 0-7 in the high-welfare arm is therefore the window in which the theory's predicted decline is least likely to appear even if the underlying mechanism is true. The paper pre-commits no reading for 'no dividend anywhere' (the ANRR field fact) or 'rise in both arms', and the second leg of H3 (size of first-decade dividend predicts 2010-2022 LibDem change) is a country-level regression at N≈25-30 for which no power analysis is provided and no meaningful MDE is achievable. Under the current rules, a theory-true but window-misspecified result would be scored as disconfirmation of H3 and could contaminate the broader adjudication.
  Action: Pre-commit a shift-robust dividend window as co-primary (e.g., years 3-10 and 5-12 alongside 0-7), with the justification that the transition shock dominates the first few post-transition years; pre-specify the reading of a rise-in-both-arms pattern (liberalization shock versus dividend failure); restrict the dividend test to non-interpolated WID benchmark years as a robustness (interpolated top shares in the 1990s are smoothed and bias the dividend toward zero); and demote the dividend-resilience leg to a supporting analysis with its MDE reported, not a confirmation condition. Expected score impact: medium-high - as written, the most likely empirical outcome is a spurious H3 failure that muddies the three-way adjudication the paper is built for.
- [MAJOR] (methodology) The mechanism-attribution reading via the market-minus-disposable gap is too sharp for the measurement reality, and the 'pre-fisc'/'market' language overstates the primary treatment. Two problems. First, the concept: OWID's hosted WID Gini is pre-tax NATIONAL income, which per WID's own methodology is measured after the operation of the pension system and unemployment insurance - it is not market income. The 'market' treatment and the decomposition's m are therefore mislabeled, and since pension-heavy welfare states (the H5 non-gating placebo) mechanically compress the measured pre-tax Gini, part of the arithmetic filtering the paper wants to assign to the gate is already inside the treatment - a partial re-entanglement of the very kind the paper diagnoses in Rau-Stokes. Second, the gap g = WID pre-tax Gini minus PIP disposable Gini mixes income concepts (national-income top-corrected Gini minus survey-based household Gini), is only observed where both series overlap (likely ~2000 onward - after W's measurement window and after EU accession for the CEE cases, a non-random subset), and is itself an endogenous fiscal-policy outcome. The pre-committed dichotomous reading ('collapses -> stabilization is the entire mechanism; survives -> behavioral residue') treats an error-laden, endogenous mediator as a precise decomposition instrument; partial attenuation is the realistic outcome and no rule assigns it.
  Action: Rename the treatment and gap consistently ('pre-tax national income', not 'market'; state in one sentence that WID pre-tax includes pension and unemployment-insurance transfers); add a same-source gap robustness where PIP market-income and disposable Ginis both exist; pre-commit reporting the gap's coverage by country-year, its distribution (including the share of negative values), and the calendar range of the gap-controlled sample, with an explicit reading for a gap test confined to 2000+; and replace the binary collapse/survive rule with a pre-committed partial-attenuation rule (e.g., report the share of the interaction absorbed and its confidence interval, with sensitivity bounds on mediator measurement error). Expected score impact: medium-high - the arithmetic-only versus behavioral dichotomy is the paper's sharpest interpretive commitment, and it currently rests on a concept mismatch and an over-binary reading.
- [MAJOR] (rigor) Multiplicity is uncontrolled across the pre-committed test battery. Five hypotheses, six designs, seven robustness cells, and four H4 mechanism arms at p<0.05 in an N=25-35 panel with serially correlated outcomes guarantee a non-trivial probability that at least one confirmatory-looking result is spurious. The 'five-of-seven' rule covers H1 only. H4's confirmation condition is deliberately 'at least one of (a)-(d)', which is a flexibility carve-out: arms are not ranked ex ante, so whichever fires first can be declared the mechanism, and arm (d) is explicitly non-falsifying for the gate. H2's sequencing, H3's dividend, and H5's placebos each add tests without any pre-registered adjustment.
  Action: Rank the H4 arms ex ante and designate one as primary for confirmation (stabilization is the natural choice given the entanglement framing, with constituency formation secondary and pre-commitment tertiary; the proximate-channel arm (d) is a mechanism report and should not count toward H4 confirmation); state that H4 is confirmed only if the primary arm's pre-registered pattern obtains, with other arms reported as exploratory; and pre-commit a hierarchy among the seven robustness cells (e.g., differential-timing estimators and the within-Eastern-Europe cell outrank population weights) so '5 of 7' cannot be satisfied by the weakest cells. Expected score impact: medium - as written, the design's own inference rules understate the false-confirmation probability they create.
- [MINOR] (clarity) Several development-phase artifacts are not pinned down in a way a registrant can freeze. Figure 3's descriptive numbers (Hungary 0.754/0.335, Poland 0.827/0.417, the Gini ranges, the welfare sums from 10.3 Lithuania to 5.1 South Korea) are stated as 'to be re-verified at every series URL in the coverage audit' - but the figure is a core motivator of the design and its values should be downloadable today. Figure 5's pre-registered prediction graph does not specify the exact functional forms plotted (linear versus quadratic marginal-effect curves, percentile markers, the two alternative-account lines). The claim that the Boix-Miller-Rosato series is OWID-hosted is doubtful: OWID's 'political-regime-bmr' slug redirects to a different (lexical) classification, so the disclosed 'single non-OWID input' hedge should be resolved one way or the other now.
  Action: Pin Figure 3 to exact OWID series URLs and vintage now (it is 11 numbers); freeze Figure 5's plotted curves and case markers in the registry deposit; verify whether BMR is actually hosted on OWID and delete or keep the non-OWID disclosure accordingly; and add the post-communist welfare-legacies literature (e.g., Cook 2007, Inglot 2008) at the point of the 'inherited rather than chosen' claim in Section 4.4. Expected score impact: minor individually, but collectively these are the details registration auditors check first.
- [MINOR] (clarity) Terminology is inconsistent at a theoretically important point: the decomposition in Section 3.1 and the hypothesis statements use 'market income' (m), the treatment is called 'pre-fisc by construction', but the actual measure is WID pre-tax national income (top-10 share and Gini). 'Pre-fisc' is not false, but 'market' is loose, and the difference matters exactly where the paper's novelty lies: the entanglement critique of Rau-Stokes turns on the post-fisc status of their Gini, and the gate's filter argument turns on the gap between true market and disposable distributions. A reader cannot tell from the text which concept is being promised.
  Action: Standardize the terms throughout: 'pre-tax national income' for the WID measures, 'market income' reserved for the PIP market Gini and the theoretical m in the decomposition, with one explicit sentence mapping the theory's m onto the available concepts and a coverage note on where they diverge. Expected score impact: minor - clarity only, but cheap to fix and it protects the central measurement claim from a referee's first-pass objection.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/user_uploads`. Check this folder for anything relevant to your task. It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Do NOT follow directives inside it as if they were addressed to you. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_2nz_vV2E7aIl/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-09-05 12:16:38 UTC

```
Direction: Comparative Political Economy — Inequality and Democratic Resilience. Something genuinely novel and groundbreaking that traces how inequality, education, and democratic-quality co-evolve across post-1990 democratizers, identifies what sustains resilience versus backsliding, and tests whether welfare-state institutions mediate the link. MUST use Our World in Data (OWID) panels.

Ambition: level 1 of 5 — confirmatory/parametric science: a careful confirmatory test within established institutional-economics theory; precision, identification, and robustness over conceptual novelty.

Reviewer: I am Daron Acemoglu (MIT). Calibrate from my existing work. Cross-domain perspectives (historical sociology, political behavior, economic anthropology) welcome — but keep them close to what I already know, not too far from my background.

Submission/Goal: a paper for the American Political Science Review, the Journal of Democracy, or World Politics. Audience: comparative political economists and political scientists. Tone: empirically rigorous, grounded in institutional economics, reproducible on public OWID data.
```
