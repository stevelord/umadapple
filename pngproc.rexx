/* png2ilbm processor - needs c:png2ilbm to work */

DO i = 10 To 15;
x = C2D(i);
SAY x;
SAY 'ADDRESS command "copy pngs/ba_320_240_30fps_' || x || '.png';
END