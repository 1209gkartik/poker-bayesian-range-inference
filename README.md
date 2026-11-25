# Bayesian Poker Opponent Modelling

An educational probability model using hypothetical hand-strength categories, not real player data or a gambling system.

Run `python analysis.py` (Python 3.9+, no dependencies). Results.csv varies the assumed probability of a weak hand betting and reports posterior probabilities, showdown equity and hypothetical expected value in abstract chips.

Bayes: posterior = prior × likelihood / sum of all weighted priors. Prior strong/medium/weak = .2/.5/.3; bet likelihoods = .8/.4/.2. After a bet the weights are .16/.20/.06, total .42. Posterior = .381/.476/.143. Assumed showdown equities are .15/.50/.80, giving weighted equity about .410. For a terminal call costing 50 into a current pot of 100 (including opponent bet), EV = equity × 100 − (1−equity) × 50. No future betting or rake; ties are abstracted into equity. Sensitivity analysis varies weak-hand bet likelihood from .1 to .9, holding other assumptions fixed.

Limitations: categories are not actual card combinations; likelihoods and equities are invented for demonstration, not calibrated. No claim of profitability or prediction accuracy. Next step: estimate likelihoods from consented or public research data, use card removal and actual hand equities, and validate on held-out observations.

Interview: explain prior versus likelihood versus posterior, normalization, sensitivity, and why assumptions dominate results. The transferable idea is updating beliefs under uncertainty.
