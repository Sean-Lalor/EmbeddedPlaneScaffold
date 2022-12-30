"""planeMovement.py is a modular file for planeMain that contains all of the movement
    sets that a plane would require.

    These are based on parts I do not have, I have made the assumption that by varying
    the voltage applied to the fin motor it would change the adjustment like the scaling of an
    PWM (Pulse Wave Modulator)
    
    How do compound movements get considered :Could use a Switch????

    Options table Roll, Yaw & Nose
    --------------------------------
    | Setting  | FinSetting (H,M,L)|
    | NULL     | [M,M,M,M,M]       |
    | RL+YL+RN | []
    | RL+YL+DN | []
    | RL+YR+RN | []
    | RL+YR+DN | []
    | RR+YL+RN | []
    | RR+YL+DN | []
    | RR+YR+RN | []
    | RR+YR+DN | []
    | RL+YL    | []
    | RL+YR    | []
    | RL+RN    | []
    | RL+DN    | []
    | RR+YL    | []
    | RR+YR    | []
    | RR+RN    | []
    | RR+DN    | []
    | YL+RN    | [H,H,H,H,H]
    | YL+DN    | [L,L,L,L,H]
    | YR+RN    | [H,H,H,H,L]
    | YR+DN    | [L,L,L,L,L]
    | RL       | [H,L,H,L,M]
    | RR       | [L,H,L,H,M]
    | YL       | [M,M,M,M,H]
    | YR       | [M,M,M,M,L]
    | RN       | [H,H,H,H,M]
    | DN       | [L,L,L,L,M]


    note FinSetting is LF, RF, LR, RR, RT

    Author: Sean Lalor
    Start Date: 29/12/2022"""

RollLeft() {
    #Sets the fins of the plane to roll Anti-Clockwise

    #Set GPIO LeftFront: High
    #Set GPIO Right Front: Low
    #Set GPIO Left Tail: High
    #Set GPIO Right Tail Low

}

RollReft() {
    #Sets the fins of the plane to roll Clockwise

    #Set GPIO LeftFront: High
    #Set GPIO Right Front: Low
    #Set GPIO Left Tail: High
    #Set GPIO Right Tail Low
}

YawLeft() {
    #Sets the top tail fin of the plane to list the plane lazily to the left

    #TopTail: High (Set to the Left)
}

YawRight() {
    #Sets the top tail fin of the plane to list the plane lazily to the left

    #TopTail: Low (Set to the Right)
}

RaiseNose() {
    #Set all horozontal set of fins to high 

    #Set GPIO LeftFront: High
    #Set GPIO Right Front: High
    #Set GPIO Left Tail: High
    #Set GPIO Right Tail High
}

DropNose() {
    #Set all horozontal set of fins to low 

    #Set GPIO LeftFront: Low
    #Set GPIO Right Front: Low
    #Set GPIO Left Tail: Low
    #Set GPIO Right Tail Low
}