.. SDES documentation master file, created by
   sphinx-quickstart on Sat Nov 19 20:17:40 2016.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Iris based Biometric identification system
==========================================

Here we are trying to implement a Iris based biometric identification which can verify the eye image for a person by comapring that eye image withh the stored eye images for that person belonging to a particular image databse. For our work we have a directory named "Input_databse" works as the image databse. This directory contain many directories where name of each subdirectory corresponds to name of each person of whom the eye iamge is stored in that directory. Each subdirectory contains an image for the left eye for that person and an image for the right eye of that person. Besides checking we have kept a provision so that when a new person wants to enter his/her eye image then that eye image will be stored in a subdirectory corresponding to the name of that new person.

**Inbuilt modules:**


   skiimage 

   PIL 

   OpenCV or cv2 

   numpy 

   matplotlib


**Contents:**


.. toctree::
   :maxdepth: 2

   main
   imworks
   iris
   pupil
   locate
   morph
   rectangulate
   feature_vec
   hamming
   gui


.. Indices and tables
.. ==================

.. * :ref:`genindex`
.. * :ref:`modindex`
.. * :ref:`search`

