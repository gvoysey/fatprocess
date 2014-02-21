fatprocess
==========

Parser for converting Health Cubby data into a useful form.

Health Cubby is a now-deprecated app published by App Cubby (now Contrast).  Wheras Gas Cubby got absorbed by Fuelley, this was just abandoned. 

This Python script (2.7.x tested) takes as an input the CSV file Health Cubby emails to you that is a complete log of all activities (workouts, weigh-ins, measurements, etc ... ).  As an output, it returns a two-column CSV containing timestamps and weights only, suitable, for instance, to import into Google Charts and thereby preserve historical weight trend data in one's own hand-rolled weight tracking application. 
