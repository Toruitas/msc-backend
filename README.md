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

It's clear now. The increasingly entrenched socio-political divisions across Western countires pose the most serious threat to... well it wouldn't be too far fetched to say the continued existence of some nations. During the 2020 US Presidential elections, a common question about the result was "Could there be another civil war?" As an American, that doesn't seem like a question you ask a society with broadly accepted values and opinions. No, that's a question asked only when division are so deep they seem impossible to bridge. 

Humans have a biological attraction to bad news. Our monkey brains want to know where every threat is coming from. Remember the old saying "If it bleeds it leads?" First with 24/7 Cable TV and now with the internet, the bleeding has reached new heights. It's gone beyond blood into blood feuds. The news is (in some circles at least) less something to inform, and instead something to push an agenda. 1984 had it wrong. 2 minutes of hate doesn't begin to compare with the onslought of anger Fox News broadcasts daily.

Companies and political parties are not learning that this trend is dangerous. They're learning it is profitable. A divided people is weak and captive.

What about us? We, the people who are flooded by divisive language. What can we do?

Let's just avoid the bad, divisive, controversial news.

This project is an effort to do that, starting by using Machine Learning to identify which submissions on reddit.com/r/news are bad, divisive, and controversial. It's not perfect, but if we can be nudged in a way to read fewer stressful news articles about how bad this or that group is, we'll be better off. 

## Project Journal

### Research stage

The original intent of the project was to identify toxically divisive language in the media, and make it clear to the reader that it was potentially written to persuade them that a certain group or idea was bad. It is not a subject that has a lot of direct research, although there is significant research on a similar field: Fake News identification. Perhaps the focus on fake news is due to a bit of secret guilt, as who is it that creates the software that write fake news? We programmers.

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

It's also important not to neglect the author. Frequently, the author's opinion bleeds into the content, and negative sentiment about an individual/group/topic will be biased. Not only would the author be biased in this particular article, but also their whole writing history, and further the author's publication(s). Ideally, the author and publications would be included in the group arithmetic. Again, this would be boosted significantly by deeper datamining to build a relationship graph. With this, perhaps some "fair and balanced" news sources could be outed as nothing more than propaganda channels coordinating with each other to brainwash.

There are techniques regularly used in persuasive writing and speaking. By combining identification of these techniques with sentiment analysis and named entity recognition, it would be possible to see when the author is trying to convince the reader (e.g.) someone is bad, versus merely stating facts that the person did bad things.

All of these would have to be done at the sentence-part, sentence, and complete article-levels. Some, even beyond, when a relationship graph or author/publication history come into play.

Finally, this would have to utilize unsupervised methods as much as possible to be robust to new information coming in.



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

