Mario the Telemetrist
=====================

![telemetrist](https://raw.github.com/snobu/Mario-the-Telemetrist/master/telemetrist.png)

Fork of [**justinmeister**](https://github.com/justinmeister/Mario-Level-1)'s mesmerising, high fidelity Super Mario Bros made with Pygame. Original repo here: https://github.com/justinmeister/Mario-Level-1.

Added in code to send telemetry info to Azure Application Insights and Event Hubs.

### Telemetry setup

1) Edit `data/telemetry/eventhub.py`. Fixup these vars:

```
namespace = 'breakingnews'
eventhubname = 'marioevents'
sasname = 'send'
```

2) Add Application Insights instrumentation key and Event Hub SAS key into:

```
data/telemetry/key_ai
data/telemetry/key_eh
```

E.g.:

key_ai:
```
7e0aa72b-XXXX-XXXX-XXXX-XXXXXXXX668
```

key_eh:
```
uKXXXXXXXXXXXXXXXXXXXXXXXncCtCIGBvrw=
```
Launch game with:
```
$ ./mario_level_1.py
```
or
```
$ python ./mario_level_1.py
```

Original README follows:

Super Mario Bros Level 1
------------------------
An attempt to recreate the first level of Super Mario Bros.

![screenshot](https://raw.github.com/justinmeister/Mario-Level-1/master/screenshot.png)

**CONTROLS:** 

Arrow keys for direction

**'a'** for jump

**'s'** for action (fireball, run)


**DEPENDENCIES:**

Pygame 1.9.1 (Python 2)

Pygame 1.9.2 (Python 3) - a little trickier to get going.

To install dependencies for Python 2.x:

	pip install -r requirements.txt

**VIDEO DEMO:**

http://www.youtube.com/watch?v=HBbzYKMfx5Y
   
**DISCLAIMER:**

This project is intended for non-commercial educational purposes.
