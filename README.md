# Image-Sentence similarity
*Charlie Kruczko 15-Aug-19*

This is mostly a fork of this repo:
https://github.com/sgrvinod/a-PyTorch-Tutorial-to-Image-Captioning

Combined with spacy's recently released transformer models.


### Achieved
- Image Captioning, CNN encoder, RNN decoder with attention.
- Sentence Similarity, done simply with spacy in python. Transformers appeared promising, but the spacy python transformer library seems to be a bit unstable.
- Gained some familiarity with flask, although not quite enough to get it working with Heroku.


### Future Work
- Testing the web app. No tests have been written yet.
- Creating an API for use, including options like return `k` best captions for an image.
- Experiment with different image encoders, resnet101 has been used, but as of recent efficientnets seem to be more powerful and may gain better results.
- Try using transformer based approaches for sentence similarity, these are capable of having a better contextual understanding.
- Fine tuning of the models, incorperation of better word vectors into the RNN.
- Celebrity detection, from the resnet101 encoded images final tensor of (1, 2048, 14, 14), many photos in news include celebrities.
  - Find areas with faces.
  - Do person recognition on each face, there may be multiple faces in an image.
  - Combine this with the attention mechanism, this focuses on specific image regions while captioning, so rather than a sentence like: "A man shakes a woman's hand", it might read "Donald Trump shakes Theresa May's hand.". ToDo: Explore named entity recognition in NLP / CV.
- Test time augmentation, including rotations, noise, cropping, skewing etc, unsure how well the system performs when it gets images that may come in at 90degrees due to being taken in portrait mode.
