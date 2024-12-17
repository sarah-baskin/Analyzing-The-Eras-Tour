# The Eras Tour: Investigating the Validity of Music Sentiment Analysis through the Case Study of Taylor Swift

Updated: 12.16.2024

## Introduction and Project Motivation

With Taylor Swift seemingly on top of mind wherever we turn (whether it's from news of her just recently ended incredibly successful international tour, images of her and Travis Kelce circling online, or her astoundingly amazing album sales), it's clear that she has had a profound impact on the popular culture of today. Incidental to this is the increasingly relevancy of the distinct 'eras' in her music. It is a concept that she has not only built her tour around, but one that guides peoples' interaction with her past and recent work.

But the realization of these eras is often much less-defined in practice than in theory. Which albums belong to which era? How should these eras be described? What specific lexical, tonal, stylistic, and musical markers should be used to differentiate one from another? Even the most hardcore of Swifties might struggle to answer those questions, which I find increasingly interesting. Her music definitely _has_ changed over time, but at what point did country become pop? At what point did bubblegum make way for pessimistic introspection?

Many of these ideas relate to the concept of Automatic Sentiment Analysis (ASA), an emerging field in Natural Langauge Processing. Also known as Opinion Mining (OM), ASA seeks to quantify the sentiment and emotion of a text, traditionally in the form of reviews or tweets. As of late, however, applications are shifting into a more literary gear, with increasing numbers of studies of SA in regards to books, poetry, and music.

Music specifically occupies a uniquely multi-faceted place in this hierarchy. It stands at the cross roads of increasingly technological productions, star personas, psychology, musicology, emotionality, and genre. It is music that is the most likely place where people will turn to find comfort, sadness, rage-bait, and self-confidence. Music as a topic in ASA has wildly exploded, however there are still many questions about the current state of the field's potential to actually get to the bottom of sentiment in such subjective mediums.

With this project, I have tried to do some of that initial investigation into the less-trustworthy side of music ASA, combining stylometric (style, lexical, and feature counts -- such as word length and profanity) with computational approachs. My goal has been to see just how consistent competing methods and models are at accomplishing the task of sentiment analysis, and the questions we can ask about music SA as a result.

Taylor Swift's discography serves as the conduit and jumping off point for this study.

## Project Description

This project was undertaken as part of my _LING 195: Introduction to Research in Linguistics or Computational Linguistics_ class at Brandeis Unviersity. The end goal of the semester is to produce a journal article about the subject matter.

Within this repo, you will find all of the individual components that I used to run the experiment as well as write my paper.

[Song Data](songs.csv) - The original song data as loaded from [shaynak](https://github.com/shaynak/taylor-swift-lyrics). Only songs from the original releases of albums (not special releases or features on other artists' work) were considered in analysis. "From the Vault" songs were excluded, but the data took from "Taylor's Version" releases for the appropriate albums.

[Data Prep and Stylometric Analysis](Stylometric_Analysis.ipynb) - A walkthrough of how I took the original data, tokenized it, prepped it, and performed analysis for the stylometric features of interest (total word count, unique word count, word length, profanity, first + second person pronoun use). I then saved the tokenized data to [this folder](songs_excl_ftv)

[VADER Analysis](Vader_Sentiment_Analysis.ipynb) - Sentiment analysis of the lyric data using [VADER](https://github.com/cjhutto/vaderSentiment)

[TextBlob Analysis](TextBlob_Sentiment_Analysis.ipynb) - Sentiment analysis of the lyric data using [TextBlob](https://textblob.readthedocs.io/en/dev/index.html)

[AFINN Analysis](Afinn_Sentiment_Analysis.ipynb) - Sentiment analysis of the lyric data using [AFINN](https://darenr.github.io/afinn/)

[Graphs](graphs) - The graphs from the various analyses, put into a neat folder for ease of access

[Final Paper](The_Eras_Tour.pdf) - my final paper, with my analysis of the graphs and my complete literature review


## Running the Project on Your Machine

Ensure that all of the necessary libraries are imported on your machine, but aside from that it should just be a simple matter of forking the repo.

## How to Use the Project

Use the various tools already developped in order to perform sentiment analysis on other musical artists, or introduce additional metrics and models that are better able to address specific sentiment concerns in the work of Taylor Swift.

## Credits

@shaynak
@cjhutto
@darenr
