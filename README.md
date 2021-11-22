# knowledge_tracing
Bayesian Knowledge Tracing Example for 100 French Words

To start learning: 
```
python learn.py
```
* Uses simple bayes filter to update probability of knowing a word
* Adds a decay to model forgetting (tunable, use plot_decay.py to see the effects over time)
* Tunable params: pS (prob of a slip), pT (prob of learning a word after seeing it), Working memory size (learn 5 words and move on),
* Tunable: New word prob (how well do we need to know words before learning new ones into working memory?)
