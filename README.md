# Belt/chain center distance calculator

## Installation
Download and copy the centerDistCalulator folder to your PC. The default location for scripts on Windows is "C:\Users\[USER]\AppData\Roaming\Autodesk\Autodesk Fusion 360\API\Scripts", however the folder can be placed anywhere.

In the design workspace, go to the tools tab, select 'Scripts and Add-Ins' and select your folder location.

![Dialog Image](https://raw.githubusercontent.com/ddaners/fusion-360-timing-belt-calculator-script/main/resources/folderSelect.PNG)


## Usage
From the 'Scripts and Add-Ins' dialog (default keyboard shortcut to open this is shift-s), select the script and press run. This will automatically create the following paramaters:

### Inputs
- z1(_n) [no units]: Number of teeth on first pulley/sprocket
- z2(_n) [no units]: Number of teeth on second pulley/sprocket
- z3(_n) [no units]: Number of teeth/linkages on belt/chain
- pitch(_n) [mm]: Belt/chain pitch
### Outputs
- d1(_n) [mm]: Pitch diameter of first pulley/sprocket
- d2(_n) [mm]: Pitch diameter of second pulley/sprocket
- cdist(_n) [mm]: Resulting ideal center distance,

Make any necesary changes to the inputs and RE-RUN THE SCRIPT! If the script is not re-run, the pitch diameters and center distances will not be updated. The script can be run again at any time to recompute any changes.

If more than one timing pulley or chains are present, by creating the variable "numPulleys" with no units, the script will create more paramaters. Using the d1, d2 and cdist output paramaters a neat sketch can be created with two circles, two tangent lines and a centerline to drive part geometry. If the paramaters are changed and the script is run again this will automatically update the paramaters and your sketch. An example of such a sketch with two different timing pulley systems can be seen below:

![Example Image](https://raw.githubusercontent.com/ddaners/fusion-360-timing-belt-calculator-script/main/resources/pulleyExample.PNG)
