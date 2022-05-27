import streamlit as st
import re
import PyPDF2
import nltk
from PyPDF2 import PdfFileReader
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords 
from string import punctuation
from googletrans import Translator
