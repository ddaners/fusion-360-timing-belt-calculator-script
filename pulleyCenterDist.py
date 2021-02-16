#Author-ddaners
#Description-Center distance calculator

import adsk.core, adsk.fusion, adsk.cam, traceback

import math

def solveCenterDist (z1, z2, z3, p):
    d1 = z1 * p / math.pi
    d2 = z2 * p / math.pi
    dmin = (d1 + d2)/2

    d = dmin
    err = 1
    i = 0

    while abs(err) > 0.00001:
        i += 1
        theta = math.asin(abs(d1 - d2) / (2 * d))

        if z1 > z2:
            c1 = math.pi * d1 * (180 + math.degrees(theta) * 2) / 360
            c2 = math.pi * d2 * (180 - math.degrees(theta) * 2) / 360
        else:
            c1 = math.pi * d1 * (180 - math.degrees(theta) * 2) / 360
            c2 = math.pi * d2 * (180 + math.degrees(theta) * 2) / 360
        
        if z1 == z2:
            d3 = d
        else:
            d3 = abs(d1 - d2) / math.tan(theta)
        
        err = c1 + c2 + d3 - z3 * p
        d = d - err / 2
    
    return d

def run(context):
    app = adsk.core.Application.get()
    ui  = app.userInterface
    design = app.activeProduct

    try:
        numPulleys = 1
        if design.userParameters.itemByName('numPulleys'):
            numPulleysParam = design.userParameters.itemByName('numPulleys')
            numPulleys = int(numPulleysParam.value)
        if numPulleys == 1:
            ui.messageBox('Pulley center distance calculator\n {} belt/chain found for computation'.format(numPulleys))
        else:
            ui.messageBox('Pulley center distance calculator\n {} belts/chains found for computation'.format(numPulleys))

        while numPulleys >= 1:

            if numPulleys == 1:
                tail = ''
            else:
                tail = '_' + str(numPulleys)

            # Get input variables (returnds NULL if not yet defined)
            z1Param = design.userParameters.itemByName('z1' + tail)
            z2Param = design.userParameters.itemByName('z2' + tail)
            z3Param = design.userParameters.itemByName('z3' + tail)
            # Get output variables (returnds NULL if not yet defined)
            pitchParam = design.userParameters.itemByName('pitch' + tail)
            d1Param = design.userParameters.itemByName('d1' + tail)
            d2Param = design.userParameters.itemByName('d2' + tail)
            cdistParam = design.userParameters.itemByName('cdist' + tail)

            # If input variables don't exist (are NULL), create them
            if not z1Param:
                design.userParameters.add('z1' + tail, adsk.core.ValueInput.createByReal(25), '', "Num of teeth on first pulley/sprocket")
                z1Param = design.userParameters.itemByName('z1' + tail)
            if not z2Param:
                design.userParameters.add('z2' + tail, adsk.core.ValueInput.createByReal(12), '', "Num of teeth on second pulley/sprocket")
                z2Param = design.userParameters.itemByName('z2' + tail)
            if not z3Param:
                design.userParameters.add('z3' + tail, adsk.core.ValueInput.createByReal(35), '', "Num of teeth/links on belt/chain")
                z3Param = design.userParameters.itemByName('z3' + tail)
            if not pitchParam:
                design.userParameters.add('pitch' + tail, adsk.core.ValueInput.createByReal(0.5), 'mm', "Belt/chain pitch")
                pitchParam = design.userParameters.itemByName('pitch' + tail)
            # If output variables don't exist (are NULL), create them
            if not d1Param:
                design.userParameters.add('d1' + tail, adsk.core.ValueInput.createByReal(2.5), 'mm', "Pitch diameter of first pulley/sprocket")
                d1Param = design.userParameters.itemByName('d1' + tail)
            if not d2Param:
                design.userParameters.add('d2' + tail, adsk.core.ValueInput.createByReal(1.2), 'mm', "Pitch diameter of second pulley/sprocket")
                d2Param = design.userParameters.itemByName('d2' + tail)
            if not cdistParam:
                design.userParameters.add('cdist' + tail, adsk.core.ValueInput.createByReal(10), 'mm', "Pulley/sprocket center distance")
                cdistParam = design.userParameters.itemByName('cdist' + tail)


            # Solve for center distance
            cdist = solveCenterDist(float(z1Param.value), float(z2Param.value), float(z3Param.value), float(pitchParam.value))
            # Display results
            ui.messageBox("Pulley {} results:\n\nINPUTS:\nz1: {}\nz2: {}\nz3: {}\npitch: {} mm\n\nOUTPUTS:\nd1: {} mm\nd2: {} mm\ncdist: {} mm".format(
                numPulleys,
                int(z1Param.value),
                int(z2Param.value),
                int(z3Param.value),
                round(pitchParam.value * 10, 3),
                round(float(d1Param.value) * 10, 3),
                round(float(d2Param.value) * 10, 3),
                round(cdist * 10, 3)))
            # Write results
            d1Param.value = float(z1Param.value) * float(pitchParam.value) / math.pi
            d2Param.value = float(z2Param.value) * float(pitchParam.value) / math.pi
            cdistParam.value = cdist

            numPulleys -= 1

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
