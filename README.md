# Msc Thesis Project Main Repository

Msc Creative Computing 2019-2020 Msc Final Thesis Project

By: Stuart Leitch

Supervisor: Mick Grierson

Date: November 27th, 2020

## Table of Contents:
* Companion Repositories
* Installation Instructions
* Introduction
* Project Journal
* Apache notes
* Useful links

## Companion Repositories
1. [Jupyter Notebooks](https://github.com/Toruitas/msc-notebooks)
2. [Backend Server](https://github.com/Toruitas/msc-backend)
3. [Chrome Extension](https://github.com/Toruitas/msc-extension)

## Installation Instructions
### Backend server

Just your typical Python setup - using either venv or Py Poetry. 

Linux/Mac instructions are as follows:
1. `git clone https://github.com/toruitas/msc-backend mscbackend`
2. `cd mscbackend`
3. `python3 -m venv .venv`
4. `source .venv/bin/activate`
5. `pip install -r requirements.txt`
6. Decompress the classifier so that the .pkl file is in the same folder as everything else. `tar -xf final-classifier-2.tar.xz`
7. `export FLASK_APP=app.py`
8. `export FLASK_ENV=development`
9. `flask run`
10. Wait a few minutes for the model to load. It will print "Loading machine learning model." in the console.

### Chrome Extension
0. If you're in mscbackend, `cd ..`
1. `https://github.com/Toruitas/msc-extension mscext`
2. `cd mscext`
3. Open Chrome and in the URL bar, navigate to `chrome://extensions/`
4. In the upper-right corner, enable Developer Mode.
![Dev mode toggle](./Developermode.png)
5. On the new navigation bar that enabling Developer Mode has revealed, click "Load unpacked."
6. Find and select the folder `mscext`
7. That's installation complete.

### After installation completes
1. In Chrome, go to [old.reddit.com/r/news](old.reddit.com/r/news)
2. Wait for a while for the titles to be sent to the Flask server for predictions.
3. See the titles change! Beware entering the comments section! It might just make you feel worse about humanity.

## Introduction

It's clear now. The increasingly entrenched socio-political tribal divisions across Western countires pose the most serious threat to... well it wouldn't be too far fetched to say the continued existence of some nations. During the 2020 US Presidential elections, a common question about the result was "Could there be another civil war?" As an American, that doesn't seem like a question you ask a society with broadly accepted values and opinions. No, that's a question asked only when division are so deep they seem impossible to bridge. 

Humans have a biological attraction to bad news. Our monkey brains want to know where every threat is coming from. Remember the old saying "If it bleeds it leads?" First with 24/7 Cable TV and now with the internet, the bleeding has reached new heights. It's gone beyond blood into blood feuds. The news is (in some circles at least) less something to inform, and instead something to push an agenda. 1984 had it wrong. 2 minutes of hate doesn't begin to compare with the onslought of anger Fox News broadcasts daily.

Companies and political parties are not learning that this trend is dangerous. They're learning it is profitable. A divided people is weak and captive.

What about us? We, the people who are flooded by divisive language. What can we do?

Let's just avoid the bad, divisive, controversial news.

This project is an effort to do that, starting by using Machine Learning to identify which submissions on reddit.com/r/news are bad, divisive, and controversial. It's not perfect, but if we can be nudged in a way to read fewer stressful news articles about how bad this or that group is, we'll be better off. 

## Project Journal

### Research stage

The original intent of the project was to identify toxically divisive language in the media, and make it clear to the reader that it was potentially written to persuade them that a certain group or idea was bad. It is not a subject that has a lot of direct research, although there is significant research on a similar field: Fake News identification and toxic language classification. Perhaps the focus on fake news is due to a bit of secret guilt, as who is it that creates the software that write fake news? We programmers.

In order to achieve this, I estimated these approaches would be necessary:

* Named entity recognition
* Topic modeling
* Positions of individuals or entities in the subject text with regards to topics
* Positive vs negative language re: individuals, groups, topics
* Identification of authors/publications who share common positions on divisive subjects
* Identify techniques of manipulation and persuasion
* Both sentence and article-level classification of the above
* Maximal usage of unsupervised learning, to prevent continuous hand-labeling of an entire corpus of data at sentence and article levels

Named entity recognition is essential to identify the target individuals and groups in a piece of text. The model would have to be able to identify new individuals and groups with new names without being explicitly told, since new characters are introduced nigh daily in this great play of life.

To begin to classify something as divisive, it's important to establish the topic about which the divisions lie. For this, topic modeling is an obvious tool to attempt to use. 

With topics and entities established, the model would then have to draw linkages between topics and individuals to determine their positions. At a minimum, this would involve sentiment analysis of these individuals, groups, and topics. At a deeper level, some relationship graphing would be useful.

It's also important not to neglect the author. Frequently, the author's opinion bleeds into the content, and negative sentiment about an individual/group/topic will be biased. Not only would the author be biased in this particular article, but also their whole writing history, and further the author's publication(s). Ideally, the author and publications would be included in the group arithmetic. Again, this would be boosted significantly by deeper datamining to build a relationship graph, alongside studies of propagation. With this, perhaps some "fair and balanced" news sources could be outed as nothing more than propaganda channels coordinating with each other to brainwash.

There are techniques regularly used in persuasive writing and speaking. By combining identification of these techniques with sentiment analysis and named entity recognition, it would be possible to see when the author is trying to convince the reader (e.g.) someone is bad, versus merely stating facts that the person did bad things.

All of these would have to be done at the sentence-part, sentence, and complete article-levels. Some, even beyond, when a relationship graph or author/publication history come into play.

Finally, this would have to utilize unsupervised methods as much as possible to be robust to new information coming in.

The links to individual research papers, articles, documentaries, interviews, and books which were a part of this process are at the end of this README.


### Modeling stage

Bias modeling 
Unsupervised
Supervised

### Pivot - Modeling stage 2

Reddit. Title. Controversial. Supervised.

### Application stage

Chrome Plugin.
Backend Flask server.

### Deployment stage
Server requirements.
Raspberry Pi.
Jetson Nano.
Stymied and alternatives.

### Future work
Maybe PhD.

## Apache Notes

`sudo gedit /etc/apache2/ports.conf`
 and change `listened` to 81

`sudo gedit mscbackend.conf`


```
<VirtualHost *:81>
    ServerName mscjetson
	WSGIDaemonProcess mscbackend user=jettoruitas group=jettoruitas threads=5
	WSGIScriptAlias / /var/www/mscbackend/app.wsgi
	<Directory /var/www/mscbackend>
		WSGIProcessGroup mscbackend
		WSGIApplicationGroup %{GLOBAL}
		Require all granted
	</Directory>
	ErrorLog /var/www/mscbackend/logs/error.log
</VirtualHost>
```

`sudo iptables -I INPUT -p tcp -m tcp --dport 81 -j ACCEPT`

`sudo netstat -tnlp | grep :81`

## Useful Links

In roughly chronological order.

* [Mark Farid Data Shadow](http://www.markfarid.com/#data1)
* [Toxic Comment Classification Challenge](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data)
* [Golbeck et al Fake News Dataset](https://github.com/jgolbeck/fakenews)
* [Tribal bias from the wild to the laboratory](https://engelsbergideas.com/essays/tribal-bias-from-the-wild-to-the-laboratory-5/)
* ['Us Vs. Them' In A Pandemic: Researchers Warn Divisions Could Get Dangerous](https://www.npr.org/sections/coronavirus-live-updates/2020/05/15/857165715/us-vs-them-in-a-pandemic-researchers-warn-divisions-could-get-dangerous)
* [Transcript: Tribal Psychology ](https://youarenotsosmart.com/transcripts/transcript-tribal-psychology/)
* [How tribal thinking has left us in a post-truth world ](https://theconversation.com/how-tribal-thinking-has-left-us-in-a-post-truth-world-69486)
* [Tribalism in Politics](https://www.psychologytoday.com/us/blog/bias-fundamentals/201806/tribalism-in-politics)
* [Word embeddings in 2020. Review with code examples](https://towardsdatascience.com/word-embeddings-in-2020-review-with-code-examples-11eb39a1ee6d)
* [23 Ways to Nudge: A Review of Technology-MediatedNudging in Human-Computer Interaction](https://dl.acm.org/doi/pdf/10.1145/3290605.3300733)
* [A Weighted Balance Model of Opinion Hyperpolarization](http://jasss.soc.surrey.ac.uk/23/3/5.html)
* [Information manipulation theory](https://en.wikipedia.org/wiki/Information_manipulation_theory)
* [CNN and Fox News are the second and third most divisive brands in the country](https://www.marketwatch.com/story/looking-for-a-fight-bring-up-these-polarizing-brands-at-the-next-mixer-2019-10-01)
* [This chart will tell you how biased your favorite news source is ](https://bigthink.com/politics-current-affairs/media-bias-chart)
* [We rate the news](https://www.adfontesmedia.com/?v=402f03a963ba)
* [A layman’s guide to detecting dangerous social media nonsense](https://www.biznews.com/undictated/2019/04/04/layman-guide-social-media-nonsense)
* [Media Companies Dominate Most Divisive Brands List, and It Keeps Getting Worse](https://morningconsult.com/2019/10/01/polarizing-brands-2019/)
* [Tracing Fake-News Footprints:Characterizing Social Media Messages by How They Propagate](https://dl.acm.org/doi/pdf/10.1145/3159652.3159677)
* [Network-based Fake News Detection: A Pattern-driven Approach](https://dl.acm.org/doi/10.1145/3373464.3373473)
* [Fake News Detection: An Interdisciplinary Research](https://dl.acm.org/doi/10.1145/3308560.3316476)
* [Polarization and Fake News: Early Warning of Potential Misinformation Targets](https://dl.acm.org/doi/10.1145/3316809)
* [Fake News vs Satire: A Dataset and Analysis](https://dl.acm.org/doi/10.1145/3201064.3201100)
* [Fake News Early Detection: A Theory-driven Model](https://dl.acm.org/doi/10.1145/3377478)
* [Combating Fake News: A Survey on Identification and Mitigation Techniques](https://dl.acm.org/doi/10.1145/3305260)
* [Tracing Fake-News Footprints: Characterizing Social Media Messages by How They Propagate](https://dl.acm.org/doi/10.1145/3159652.3159677)
* [Combating fake news: a data management and mining perspective](https://dl.acm.org/doi/10.14778/3352063.3352117)
* [Fake News Research: Theories, Detection Strategies, and Open Problems](https://dl.acm.org/doi/10.1145/3292500.3332287)
* [Fake News: Fundamental Theories, Detection Strategies and Challenges](https://dl.acm.org/doi/10.1145/3289600.3291382)
* [Identifying Biases in Politically Biased Wikis through Word Embeddings](https://dl-acm-org.arts.idm.oclc.org/doi/10.1145/3342220.3343658)
* [Neural Based Statement Classification for Biased Language](https://dl-acm-org.arts.idm.oclc.org/doi/10.1145/3289600.3291018)
* [Detecting Biased Statements in Wikipedia](https://dl-acm-org.arts.idm.oclc.org/doi/10.1145/3184558.3191640)
* [The Art of the Smear](https://getpocket.com/explore/item/the-journalist-and-the-troll-this-man-spent-two-years-trying-to-destroy-me-online?utm_source=pocket-newtab)
* [How to (Actually) Change Someone’s Mind](https://hbr.org/2020/07/how-to-actually-change-someones-mind?utm_source=pocket-newtab)
* [How an ex-YouTube insider investigated its secret algorithm](https://www.theguardian.com/technology/2018/feb/02/youtube-algorithm-election-clinton-trump-guillaume-chaslot)
* (https://www.technologyreview.com/2020/08/14/1006780/ai-gpt-3-fake-blog-reached-top-of-hacker-news/?utm_source=pocket-newtab)[https://www.technologyreview.com/2020/08/14/1006780/ai-gpt-3-fake-blog-reached-top-of-hacker-news/?utm_source=pocket-newtab]
* [Structure  and  Form:Reflections  on  a  Workby  Vladimir  Propp](https://monoskop.org/images/4/42/Levi-Strauss_Claude_1960_1984_Structure_and_Form_Reflections_on_a_Work_by_Vladimir_Propp.pdf)
* [Identifying Biases in Politically Biased Wikis through Word Embeddings](https://github.com/Mknoche/wiki_bias_embedding)
* [Experiments on the English Wikipedia](https://radimrehurek.com/gensim/wiki.html#wiki)
* [Invisible Manipulators of Your Mind](https://getpocket.com/explore/item/invisible-manipulators-of-your-mind?utm_source=pocket-newtab)
* [Political Tribes by Amy Chua](https://www.amychua.com/political-tribes-1)
* [Topic Modeling with Gensim (Python)](https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/)
* [#WhoAmI in 160 Characters? Classifying Social Identities Based on TwitterProfile Descriptions](https://djoerdhiemstra.com/wp-content/uploads/nlpcss2016.pdf)
* [Using Natural Language Processing toAutomatically Detect Self-AdmittedTechnical Debt](http://das.encs.concordia.ca/uploads/2017/01/Maldonado_TSE2017.pdf)
* [De-identification in Natural Language Processing](https://core.ac.uk/download/pdf/35346373.pdf)
* [How to solve 90% of NLP problems: a step-by-step guide](https://blog.insightdatascience.com/how-to-solve-90-of-nlp-problems-a-step-by-step-guide-fda605278e4e)
* [3 Super Simple Projects to Learn Natural Language Processing using Python](https://towardsdatascience.com/3-super-simple-projects-to-learn-natural-language-processing-using-python-8ef74c757cd9)
* [The Simple Approach to Word Embedding for Natural Language Processing using Python](https://towardsdatascience.com/the-simple-approach-to-word-embedding-for-natural-language-processing-using-python-ae028c8dbfd2)
* [Social Identity Theory](https://www.simplypsychology.org/social-identity-theory.html)
* [In-group favouritism and out-group discrimination in naturally occurring groups](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0221616)
* [Social Dominance and Social Identity in the United States and Israel: Ingroup Favoritism or Outgroup Derogation?](https://www.researchgate.net/publication/229573938_Social_Dominance_and_Social_Identity_in_the_United_States_and_Israel_Ingroup_Favoritism_or_Outgroup_Derogation)
* [Applying artificial intelligence for social good](https://www.mckinsey.com/featured-insights/artificial-intelligence/applying-artificial-intelligence-for-social-good#)
* [A Just and Comprehensive Strategy forUsing NLP to Address Online Abuse](https://www.aclweb.org/anthology/P19-1357.pdf)
* [Discovering User Groups for Natural Language Generation](https://www.aclweb.org/anthology/W18-5018.pdf)
* [In-group, Out-group Bias](https://www.units.miamioh.edu/psybersite/fans/inoutbias.shtml)
* [Using NLP to understand laws](https://towardsdatascience.com/using-nlp-to-understand-laws-95278624ae5)
* [In-Groups and Out-Groups](https://socialsci.libretexts.org/Bookshelves/Sociology/Book%3A_Sociology_%28Boundless%29/06%3A_Social_Groups_and_Organization/6.01%3A_Types_of_Social_Groups/6.1D%3A_In-Groups_and_Out-Groups)
* [How the Social Sector Can Use Natural Language Processing ](https://ssir.org/articles/entry/how_the_social_sector_can_use_natural_language_processing)
* [Predicting Political Bias with Python](https://medium.com/linalgo/predict-political-bias-using-python-b8575eedef13)
* [Predicting Political Affiliation with Natural Language Processing](https://medium.com/@jon.reynolds30/comparing-classification-models-using-lending-clubs-peer-toloan-data-615153db2124)
* [Automatic Detection of Political Opinions in Tweets](https://link.springer.com/chapter/10.1007/978-3-642-25953-1_8)
* [The Perils of Classifying Political Orientation From Text](https://www.cse.wustl.edu/~sanmay/papers/political-orientation.pdf)
* [Distinguishing topical and social groups based on common identity and bond theory](https://dl.acm.org/doi/10.1145/2433396.2433475)
* [Community detection in social networks through similarity virtual networks](https://dl.acm.org/doi/10.1145/2492517.2500299)
* [Formation Period Matters: Towards Socially Consistent Group Detection via Dense Subgraph Seeking](https://dl.acm.org/doi/10.1145/2671188.2749305)
* [Group Segregation in Social Networks](https://dl.acm.org/doi/10.5555/3306127.3331867)
* [Group Profiling for Understanding Social Structures](https://dl.acm.org/doi/10.1145/2036264.2036279)
* [Identifying and Classifying Social Groups: A Machine Learning Approach](https://link.springer.com/chapter/10.1007/3-540-34416-0_17)
* [Applying natural language processing to evaluate news media coverage of bullying and cyberbullying](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6883130/)
* [GIVING COMPUTERS A NOSE FOR NEWS: Exploring the limits of story detection and verification](https://epub.ub.uni-muenchen.de/28834/1/GivingComputersANoseForNewsPREPRINTsubmittedversion.pdf)
* [Improved topic models for social media via community detection using user interaction and content similarity](https://ieeexplore.ieee.org/abstract/document/7584770)
* [Detection and classification of social media-based extremist affiliations using sentiment analysis techniques](https://hcis-journal.springeropen.com/articles/10.1186/s13673-019-0185-6)
* [Multi-Criteria Dimensionality Reduction withApplications to Fairness](https://arxiv.org/pdf/1902.11281.pdf)
* [New Machine Learning Algorithms Reduce Bias in Identifying Groups](https://www.cc.gatech.edu/news/622219/new-machine-learning-algorithms-reduce-bias-identifying-groups)
* [Sentiment Identification in Code-Mixed Social MediaText](https://arxiv.org/pdf/1707.01184.pdf)
* [Python Named Entity Recognition - Machine Learning Project Series: Part 1](https://programmerbackpack.com/machine-learning-project-series-building-a-personal-knowledge-management-system-part-1-named-entity-recognition/)
* [Predicting Authors- Unsupervised NLP, LSA and BOW](https://www.kaggle.com/miguelniblock/predict-the-author-unsupervised-nlp-lsa-and-bow)
* [Twitter US Airline Sentiment](https://www.kaggle.com/crowdflower/twitter-airline-sentiment)
* [Unsupervised-Text-Clustering using Natural Language Processing(NLP)](https://medium.com/@rohithramesh1991/unsupervised-text-clustering-using-natural-language-processing-nlp-1a8bc18b048d)
* [Unsupervised-Text-Clustering](https://github.com/rohithramesh1991/Unsupervised-Text-Clustering)
* [[R] Hyperparameter Tuning for Transformer Models](https://www.reddit.com/r/MachineLearning/comments/ihb2gn/r_hyperparameter_tuning_for_transformer_models/)
* [Effective Machine Learning Approach to Detect Groups of Fake Reviewers](https://csce.ucmss.com/cr/books/2018/LFS/CSREA2018/ICD8036.pdf)
* [Fastai](https://course.fast.ai/)
