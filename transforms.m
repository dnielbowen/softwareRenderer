clear

vertex = [1,1,1,1]; % Homogenous coordinates

% View matrix

cameraPos = [45, 45, 45];
cameraTarget = [0,0,0];
cameraUp = [0,1,0];
cameraZ = cameraTarget - cameraPos;
cameraZ = cameraZ/norm(cameraZ);
cameraY = cross(cross(cameraZ, cameraUp), cameraZ);
cameraY = cameraY/norm(cameraY);
cameraX = cross(cameraZ, cameraY);
matView = inv([[cameraX 0]' [cameraY 0]' [cameraZ 0]' [cameraPos 1]']);

% Test data set
cX = [-1 0 0];
cY = [0 -1 0];
cZ = [0 0 1];
cP = [1 2 1];
matC = inv([[cX 0]' [cY 0]' [cZ 0]' [cP 1]']);
testP = [1 0 1];
 % Ding ding ding! [0 2 0] is the correct precomputed answer
newP = matC * [testP 1]';


projWinWidth = 2;
aspectRatio = 1;
projWinHeight = projWinWidth/aspectRatio;
projHFOV = 63;
d = projWinWidth/(2*tand(projHFOV/2));
farPlane = 1000;

matProj = [
    2*d/projWinWidth, 0, 0, 0;
    0, 2*d/projWinHeight, 0, 0;
    0, 0, (farPlane+d)/(farPlane-d), 2*d*farPlane/(farPlane-d);
    0, 0, 1, 0
];

v1w = [-1 -1 1 1]';
v1v = matView * v1w;
v1p = matProj * v1v / v1v(3); % Projection with perspective divide

matScreenScale = [
    600/2 0 0 0;
    0 -600/2 0 0;
    0 0 1 0;
    0 0 600/2 1
];

mShiftTranslate = [
    1 0 0 1;
    0 1 0 1;
    0 0 1 0;
    0 0 0 1
];

mHalf = [
    0.5 0 0 0;
    0 0.5 0 0;
    0 0 1 0;
    0 0 0 1
];

mScale = [
    600 0 0 0;
    0 -600 0 0;
    0 0 1 0;
    0 0 0 1
];

mYOffset = [
    1 0 0 0;
    0 1 0 600;
    0 0 1 0;
    0 0 0 1
];

v1s = mYOffset*mScale*mHalf*mShiftTranslate*v1p;
