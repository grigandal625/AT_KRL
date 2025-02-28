# Generated from /app/at_krl_parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,108,736,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,
        7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,
        13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,
        20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,
        26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,
        33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,
        39,2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,2,
        46,7,46,2,47,7,47,2,48,7,48,2,49,7,49,2,50,7,50,2,51,7,51,2,52,7,
        52,2,53,7,53,2,54,7,54,2,55,7,55,2,56,7,56,2,57,7,57,2,58,7,58,2,
        59,7,59,2,60,7,60,2,61,7,61,2,62,7,62,2,63,7,63,2,64,7,64,2,65,7,
        65,2,66,7,66,2,67,7,67,2,68,7,68,2,69,7,69,2,70,7,70,2,71,7,71,1,
        0,3,0,146,8,0,1,1,4,1,149,8,1,11,1,12,1,150,1,2,5,2,154,8,2,10,2,
        12,2,157,9,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,166,8,3,10,3,12,3,169,
        9,3,1,4,1,4,1,4,5,4,174,8,4,10,4,12,4,177,9,4,1,5,1,5,1,5,5,5,182,
        8,5,10,5,12,5,185,9,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,194,8,6,1,
        7,1,7,1,7,3,7,199,8,7,1,8,1,8,1,8,3,8,204,8,8,1,8,1,8,1,8,1,8,3,
        8,210,8,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,4,10,220,8,10,11,10,
        12,10,221,1,11,1,11,1,11,1,11,3,11,228,8,11,1,11,3,11,231,8,11,1,
        12,1,12,1,12,1,12,4,12,237,8,12,11,12,12,12,238,1,12,3,12,242,8,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,1,15,4,
        15,256,8,15,11,15,12,15,257,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,3,17,275,8,17,1,18,1,18,1,
        18,3,18,280,8,18,1,19,1,19,3,19,284,8,19,1,19,1,19,1,19,1,19,3,19,
        290,8,19,1,20,1,20,1,20,3,20,295,8,20,1,20,1,20,1,20,4,20,300,8,
        20,11,20,12,20,301,1,21,1,21,1,21,3,21,307,8,21,1,22,1,22,3,22,311,
        8,22,1,22,1,22,1,22,3,22,316,8,22,1,23,1,23,1,23,1,23,1,23,1,23,
        3,23,324,8,23,1,23,1,23,3,23,328,8,23,1,23,1,23,1,23,3,23,333,8,
        23,1,24,1,24,1,24,1,24,1,24,3,24,340,8,24,1,24,1,24,1,24,1,24,1,
        24,3,24,347,8,24,1,25,1,25,1,25,1,25,1,25,3,25,354,8,25,1,26,1,26,
        1,26,1,26,1,26,3,26,361,8,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,
        3,26,370,8,26,1,27,1,27,1,27,1,27,1,27,3,27,377,8,27,1,28,1,28,1,
        28,1,28,1,28,3,28,384,8,28,1,29,3,29,387,8,29,1,29,1,29,1,30,3,30,
        392,8,30,1,30,1,30,1,31,3,31,397,8,31,1,31,1,31,1,32,3,32,402,8,
        32,1,32,1,32,1,33,1,33,3,33,408,8,33,1,33,3,33,411,8,33,1,33,1,33,
        1,33,1,33,1,33,1,33,1,33,1,33,3,33,421,8,33,1,33,1,33,3,33,425,8,
        33,1,34,1,34,1,35,1,35,1,35,3,35,432,8,35,1,36,1,36,1,37,1,37,1,
        37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,3,37,446,8,37,1,37,1,37,3,
        37,450,8,37,1,37,1,37,3,37,454,8,37,1,37,1,37,1,37,1,37,1,37,1,37,
        1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,1,37,5,37,472,8,37,
        10,37,12,37,475,9,37,1,38,1,38,1,39,1,39,1,39,1,39,1,39,1,39,1,39,
        1,40,1,40,1,40,1,41,1,41,1,41,1,41,1,41,3,41,494,8,41,1,42,1,42,
        3,42,498,8,42,1,43,1,43,3,43,502,8,43,1,44,1,44,1,44,1,44,1,44,1,
        44,3,44,510,8,44,1,44,1,44,1,44,3,44,515,8,44,1,44,1,44,3,44,519,
        8,44,1,44,1,44,3,44,523,8,44,1,44,1,44,3,44,527,8,44,1,44,1,44,1,
        44,1,44,3,44,533,8,44,1,44,1,44,1,44,1,44,3,44,539,8,44,1,44,1,44,
        1,44,1,44,3,44,545,8,44,1,44,1,44,1,44,1,44,3,44,551,8,44,5,44,553,
        8,44,10,44,12,44,556,9,44,1,45,1,45,1,45,1,45,1,45,1,45,1,45,3,45,
        565,8,45,1,45,1,45,1,45,3,45,570,8,45,1,45,1,45,3,45,574,8,45,1,
        45,1,45,3,45,578,8,45,1,45,1,45,3,45,582,8,45,1,45,1,45,1,45,1,45,
        3,45,588,8,45,1,45,1,45,1,45,1,45,3,45,594,8,45,1,45,1,45,1,45,1,
        45,3,45,600,8,45,1,45,1,45,1,45,1,45,3,45,606,8,45,5,45,608,8,45,
        10,45,12,45,611,9,45,1,46,1,46,1,47,1,47,3,47,617,8,47,1,48,1,48,
        1,48,1,48,1,48,1,48,1,48,1,48,3,48,627,8,48,1,49,1,49,1,49,1,49,
        1,50,1,50,1,50,1,50,1,51,1,51,3,51,639,8,51,1,52,1,52,1,53,1,53,
        1,54,1,54,1,55,1,55,1,56,1,56,1,57,1,57,1,58,1,58,1,59,1,59,1,59,
        1,60,1,60,1,60,1,60,1,60,1,60,3,60,664,8,60,1,60,1,60,1,60,1,60,
        1,60,1,60,1,60,3,60,673,8,60,1,60,1,60,1,60,3,60,678,8,60,1,61,1,
        61,3,61,682,8,61,1,62,1,62,1,63,1,63,1,63,1,64,1,64,1,64,1,64,1,
        64,3,64,694,8,64,1,65,1,65,1,65,1,65,1,66,1,66,1,66,1,66,4,66,704,
        8,66,11,66,12,66,705,1,67,1,67,1,67,1,67,4,67,712,8,67,11,67,12,
        67,713,1,68,1,68,1,68,1,68,3,68,720,8,68,1,68,1,68,1,68,1,68,3,68,
        726,8,68,3,68,728,8,68,1,69,1,69,1,70,1,70,1,71,1,71,1,71,8,155,
        167,175,183,221,238,257,301,3,74,88,90,72,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
        62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,92,94,96,98,100,102,
        104,106,108,110,112,114,116,118,120,122,124,126,128,130,132,134,
        136,138,140,142,0,13,1,0,43,44,1,0,15,16,1,0,13,14,1,0,103,104,2,
        0,20,20,24,26,1,0,21,23,2,0,51,54,70,72,3,0,67,67,73,73,86,86,4,
        0,55,56,58,58,62,66,80,85,5,0,49,50,60,60,68,69,74,75,78,79,3,0,
        45,45,48,48,76,77,1,0,87,100,2,0,46,46,57,58,769,0,145,1,0,0,0,2,
        148,1,0,0,0,4,155,1,0,0,0,6,167,1,0,0,0,8,175,1,0,0,0,10,183,1,0,
        0,0,12,186,1,0,0,0,14,198,1,0,0,0,16,203,1,0,0,0,18,213,1,0,0,0,
        20,219,1,0,0,0,22,223,1,0,0,0,24,232,1,0,0,0,26,245,1,0,0,0,28,249,
        1,0,0,0,30,255,1,0,0,0,32,259,1,0,0,0,34,267,1,0,0,0,36,279,1,0,
        0,0,38,283,1,0,0,0,40,294,1,0,0,0,42,303,1,0,0,0,44,308,1,0,0,0,
        46,317,1,0,0,0,48,334,1,0,0,0,50,348,1,0,0,0,52,355,1,0,0,0,54,371,
        1,0,0,0,56,378,1,0,0,0,58,386,1,0,0,0,60,391,1,0,0,0,62,396,1,0,
        0,0,64,401,1,0,0,0,66,424,1,0,0,0,68,426,1,0,0,0,70,428,1,0,0,0,
        72,433,1,0,0,0,74,453,1,0,0,0,76,476,1,0,0,0,78,478,1,0,0,0,80,485,
        1,0,0,0,82,493,1,0,0,0,84,495,1,0,0,0,86,499,1,0,0,0,88,526,1,0,
        0,0,90,581,1,0,0,0,92,612,1,0,0,0,94,614,1,0,0,0,96,626,1,0,0,0,
        98,628,1,0,0,0,100,632,1,0,0,0,102,638,1,0,0,0,104,640,1,0,0,0,106,
        642,1,0,0,0,108,644,1,0,0,0,110,646,1,0,0,0,112,648,1,0,0,0,114,
        650,1,0,0,0,116,652,1,0,0,0,118,654,1,0,0,0,120,657,1,0,0,0,122,
        681,1,0,0,0,124,683,1,0,0,0,126,685,1,0,0,0,128,688,1,0,0,0,130,
        695,1,0,0,0,132,699,1,0,0,0,134,707,1,0,0,0,136,727,1,0,0,0,138,
        729,1,0,0,0,140,731,1,0,0,0,142,733,1,0,0,0,144,146,5,105,0,0,145,
        144,1,0,0,0,145,146,1,0,0,0,146,1,1,0,0,0,147,149,5,107,0,0,148,
        147,1,0,0,0,149,150,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,
        3,1,0,0,0,152,154,3,2,1,0,153,152,1,0,0,0,154,157,1,0,0,0,155,156,
        1,0,0,0,155,153,1,0,0,0,156,158,1,0,0,0,157,155,1,0,0,0,158,159,
        3,6,3,0,159,160,3,8,4,0,160,161,3,10,5,0,161,5,1,0,0,0,162,163,3,
        12,6,0,163,164,3,2,1,0,164,166,1,0,0,0,165,162,1,0,0,0,166,169,1,
        0,0,0,167,168,1,0,0,0,167,165,1,0,0,0,168,7,1,0,0,0,169,167,1,0,
        0,0,170,171,3,34,17,0,171,172,3,2,1,0,172,174,1,0,0,0,173,170,1,
        0,0,0,174,177,1,0,0,0,175,176,1,0,0,0,175,173,1,0,0,0,176,9,1,0,
        0,0,177,175,1,0,0,0,178,179,3,120,60,0,179,180,3,2,1,0,180,182,1,
        0,0,0,181,178,1,0,0,0,182,185,1,0,0,0,183,184,1,0,0,0,183,181,1,
        0,0,0,184,11,1,0,0,0,185,183,1,0,0,0,186,187,5,7,0,0,187,188,5,102,
        0,0,188,189,3,2,1,0,189,193,3,14,7,0,190,191,3,2,1,0,191,192,3,118,
        59,0,192,194,1,0,0,0,193,190,1,0,0,0,193,194,1,0,0,0,194,13,1,0,
        0,0,195,199,3,32,16,0,196,199,3,28,14,0,197,199,3,16,8,0,198,195,
        1,0,0,0,198,196,1,0,0,0,198,197,1,0,0,0,199,15,1,0,0,0,200,201,3,
        28,14,0,201,202,3,2,1,0,202,204,1,0,0,0,203,200,1,0,0,0,203,204,
        1,0,0,0,204,205,1,0,0,0,205,209,5,33,0,0,206,207,3,2,1,0,207,208,
        5,103,0,0,208,210,1,0,0,0,209,206,1,0,0,0,209,210,1,0,0,0,210,211,
        1,0,0,0,211,212,3,20,10,0,212,17,1,0,0,0,213,214,3,22,11,0,214,215,
        3,24,12,0,215,19,1,0,0,0,216,217,3,2,1,0,217,218,3,18,9,0,218,220,
        1,0,0,0,219,216,1,0,0,0,220,221,1,0,0,0,221,222,1,0,0,0,221,219,
        1,0,0,0,222,21,1,0,0,0,223,224,5,104,0,0,224,225,5,103,0,0,225,227,
        5,103,0,0,226,228,5,103,0,0,227,226,1,0,0,0,227,228,1,0,0,0,228,
        230,1,0,0,0,229,231,5,58,0,0,230,229,1,0,0,0,230,231,1,0,0,0,231,
        23,1,0,0,0,232,233,5,38,0,0,233,236,3,26,13,0,234,235,7,0,0,0,235,
        237,3,26,13,0,236,234,1,0,0,0,237,238,1,0,0,0,238,239,1,0,0,0,238,
        236,1,0,0,0,239,241,1,0,0,0,240,242,7,0,0,0,241,240,1,0,0,0,241,
        242,1,0,0,0,242,243,1,0,0,0,243,244,5,41,0,0,244,25,1,0,0,0,245,
        246,5,103,0,0,246,247,5,52,0,0,247,248,5,103,0,0,248,27,1,0,0,0,
        249,250,5,31,0,0,250,251,3,30,15,0,251,29,1,0,0,0,252,253,3,2,1,
        0,253,254,5,104,0,0,254,256,1,0,0,0,255,252,1,0,0,0,256,257,1,0,
        0,0,257,258,1,0,0,0,257,255,1,0,0,0,258,31,1,0,0,0,259,260,5,32,
        0,0,260,261,3,2,1,0,261,262,5,34,0,0,262,263,5,103,0,0,263,264,3,
        2,1,0,264,265,5,35,0,0,265,266,5,103,0,0,266,33,1,0,0,0,267,268,
        5,8,0,0,268,269,5,102,0,0,269,270,3,2,1,0,270,274,3,36,18,0,271,
        272,3,2,1,0,272,273,3,118,59,0,273,275,1,0,0,0,274,271,1,0,0,0,274,
        275,1,0,0,0,275,35,1,0,0,0,276,280,3,38,19,0,277,280,3,48,24,0,278,
        280,3,52,26,0,279,276,1,0,0,0,279,277,1,0,0,0,279,278,1,0,0,0,280,
        37,1,0,0,0,281,282,5,9,0,0,282,284,5,102,0,0,283,281,1,0,0,0,283,
        284,1,0,0,0,284,285,1,0,0,0,285,289,3,40,20,0,286,287,3,2,1,0,287,
        288,3,118,59,0,288,290,1,0,0,0,289,286,1,0,0,0,289,290,1,0,0,0,290,
        39,1,0,0,0,291,292,3,2,1,0,292,293,5,11,0,0,293,295,1,0,0,0,294,
        291,1,0,0,0,294,295,1,0,0,0,295,299,1,0,0,0,296,297,3,2,1,0,297,
        298,3,42,21,0,298,300,1,0,0,0,299,296,1,0,0,0,300,301,1,0,0,0,301,
        302,1,0,0,0,301,299,1,0,0,0,302,41,1,0,0,0,303,306,3,64,32,0,304,
        307,3,46,23,0,305,307,3,44,22,0,306,304,1,0,0,0,306,305,1,0,0,0,
        307,43,1,0,0,0,308,310,5,42,0,0,309,311,5,7,0,0,310,309,1,0,0,0,
        310,311,1,0,0,0,311,312,1,0,0,0,312,315,5,102,0,0,313,314,5,58,0,
        0,314,316,3,88,44,0,315,313,1,0,0,0,315,316,1,0,0,0,316,45,1,0,0,
        0,317,318,3,2,1,0,318,319,5,7,0,0,319,327,5,102,0,0,320,321,3,2,
        1,0,321,323,5,12,0,0,322,324,3,2,1,0,323,322,1,0,0,0,323,324,1,0,
        0,0,324,325,1,0,0,0,325,326,3,88,44,0,326,328,1,0,0,0,327,320,1,
        0,0,0,327,328,1,0,0,0,328,332,1,0,0,0,329,330,3,2,1,0,330,331,3,
        118,59,0,331,333,1,0,0,0,332,329,1,0,0,0,332,333,1,0,0,0,333,47,
        1,0,0,0,334,335,5,9,0,0,335,339,7,1,0,0,336,337,3,2,1,0,337,338,
        5,11,0,0,338,340,1,0,0,0,339,336,1,0,0,0,339,340,1,0,0,0,340,341,
        1,0,0,0,341,342,3,2,1,0,342,346,3,50,25,0,343,344,3,2,1,0,344,345,
        3,118,59,0,345,347,1,0,0,0,346,343,1,0,0,0,346,347,1,0,0,0,347,49,
        1,0,0,0,348,349,3,58,29,0,349,353,3,66,33,0,350,351,3,2,1,0,351,
        352,3,118,59,0,352,354,1,0,0,0,353,350,1,0,0,0,353,354,1,0,0,0,354,
        51,1,0,0,0,355,356,5,9,0,0,356,360,7,2,0,0,357,358,3,2,1,0,358,359,
        5,11,0,0,359,361,1,0,0,0,360,357,1,0,0,0,360,361,1,0,0,0,361,362,
        1,0,0,0,362,363,3,2,1,0,363,364,3,54,27,0,364,365,3,2,1,0,365,369,
        3,56,28,0,366,367,3,2,1,0,367,368,3,118,59,0,368,370,1,0,0,0,369,
        366,1,0,0,0,369,370,1,0,0,0,370,53,1,0,0,0,371,372,3,60,30,0,372,
        376,3,66,33,0,373,374,3,2,1,0,374,375,3,118,59,0,375,377,1,0,0,0,
        376,373,1,0,0,0,376,377,1,0,0,0,377,55,1,0,0,0,378,379,3,62,31,0,
        379,383,3,66,33,0,380,381,3,2,1,0,381,382,3,118,59,0,382,384,1,0,
        0,0,383,380,1,0,0,0,383,384,1,0,0,0,384,57,1,0,0,0,385,387,5,10,
        0,0,386,385,1,0,0,0,386,387,1,0,0,0,387,388,1,0,0,0,388,389,5,17,
        0,0,389,59,1,0,0,0,390,392,5,10,0,0,391,390,1,0,0,0,391,392,1,0,
        0,0,392,393,1,0,0,0,393,394,5,18,0,0,394,61,1,0,0,0,395,397,5,10,
        0,0,396,395,1,0,0,0,396,397,1,0,0,0,397,398,1,0,0,0,398,399,5,19,
        0,0,399,63,1,0,0,0,400,402,5,10,0,0,401,400,1,0,0,0,401,402,1,0,
        0,0,402,403,1,0,0,0,403,404,5,102,0,0,404,65,1,0,0,0,405,407,5,42,
        0,0,406,408,5,7,0,0,407,406,1,0,0,0,407,408,1,0,0,0,408,409,1,0,
        0,0,409,411,5,27,0,0,410,405,1,0,0,0,410,411,1,0,0,0,411,412,1,0,
        0,0,412,413,5,58,0,0,413,425,3,76,38,0,414,415,3,2,1,0,415,416,5,
        7,0,0,416,417,5,27,0,0,417,418,3,2,1,0,418,420,5,12,0,0,419,421,
        3,2,1,0,420,419,1,0,0,0,420,421,1,0,0,0,421,422,1,0,0,0,422,423,
        3,76,38,0,423,425,1,0,0,0,424,410,1,0,0,0,424,414,1,0,0,0,425,67,
        1,0,0,0,426,427,7,3,0,0,427,69,1,0,0,0,428,431,5,102,0,0,429,430,
        5,59,0,0,430,432,3,70,35,0,431,429,1,0,0,0,431,432,1,0,0,0,432,71,
        1,0,0,0,433,434,3,70,35,0,434,73,1,0,0,0,435,436,6,37,-1,0,436,454,
        3,72,36,0,437,454,3,68,34,0,438,439,3,108,54,0,439,440,3,74,37,7,
        440,454,1,0,0,0,441,442,5,48,0,0,442,454,3,74,37,2,443,445,5,36,
        0,0,444,446,3,2,1,0,445,444,1,0,0,0,445,446,1,0,0,0,446,447,1,0,
        0,0,447,449,3,74,37,0,448,450,3,2,1,0,449,448,1,0,0,0,449,450,1,
        0,0,0,450,451,1,0,0,0,451,452,5,39,0,0,452,454,1,0,0,0,453,435,1,
        0,0,0,453,437,1,0,0,0,453,438,1,0,0,0,453,441,1,0,0,0,453,443,1,
        0,0,0,454,473,1,0,0,0,455,456,10,6,0,0,456,457,3,112,56,0,457,458,
        3,74,37,7,458,472,1,0,0,0,459,460,10,5,0,0,460,461,3,114,57,0,461,
        462,3,74,37,6,462,472,1,0,0,0,463,464,10,4,0,0,464,465,3,110,55,
        0,465,466,3,74,37,5,466,472,1,0,0,0,467,468,10,3,0,0,468,469,3,106,
        53,0,469,470,3,74,37,4,470,472,1,0,0,0,471,455,1,0,0,0,471,459,1,
        0,0,0,471,463,1,0,0,0,471,467,1,0,0,0,472,475,1,0,0,0,473,471,1,
        0,0,0,473,474,1,0,0,0,474,75,1,0,0,0,475,473,1,0,0,0,476,477,3,74,
        37,0,477,77,1,0,0,0,478,479,5,1,0,0,479,480,5,37,0,0,480,481,5,103,
        0,0,481,482,7,0,0,0,482,483,5,103,0,0,483,484,5,40,0,0,484,79,1,
        0,0,0,485,486,5,2,0,0,486,487,5,103,0,0,487,81,1,0,0,0,488,489,3,
        78,39,0,489,490,3,80,40,0,490,494,1,0,0,0,491,494,3,78,39,0,492,
        494,3,80,40,0,493,488,1,0,0,0,493,491,1,0,0,0,493,492,1,0,0,0,494,
        83,1,0,0,0,495,497,3,68,34,0,496,498,3,82,41,0,497,496,1,0,0,0,497,
        498,1,0,0,0,498,85,1,0,0,0,499,501,3,72,36,0,500,502,3,82,41,0,501,
        500,1,0,0,0,501,502,1,0,0,0,502,87,1,0,0,0,503,504,6,44,-1,0,504,
        527,3,86,43,0,505,527,3,84,42,0,506,507,5,48,0,0,507,509,3,88,44,
        0,508,510,3,82,41,0,509,508,1,0,0,0,509,510,1,0,0,0,510,527,1,0,
        0,0,511,512,3,108,54,0,512,514,3,88,44,0,513,515,3,82,41,0,514,513,
        1,0,0,0,514,515,1,0,0,0,515,527,1,0,0,0,516,518,5,36,0,0,517,519,
        3,2,1,0,518,517,1,0,0,0,518,519,1,0,0,0,519,520,1,0,0,0,520,522,
        3,88,44,0,521,523,3,2,1,0,522,521,1,0,0,0,522,523,1,0,0,0,523,524,
        1,0,0,0,524,525,5,39,0,0,525,527,1,0,0,0,526,503,1,0,0,0,526,505,
        1,0,0,0,526,506,1,0,0,0,526,511,1,0,0,0,526,516,1,0,0,0,527,554,
        1,0,0,0,528,529,10,5,0,0,529,530,3,112,56,0,530,532,3,88,44,0,531,
        533,3,82,41,0,532,531,1,0,0,0,532,533,1,0,0,0,533,553,1,0,0,0,534,
        535,10,4,0,0,535,536,3,114,57,0,536,538,3,88,44,0,537,539,3,82,41,
        0,538,537,1,0,0,0,538,539,1,0,0,0,539,553,1,0,0,0,540,541,10,3,0,
        0,541,542,3,110,55,0,542,544,3,88,44,0,543,545,3,82,41,0,544,543,
        1,0,0,0,544,545,1,0,0,0,545,553,1,0,0,0,546,547,10,2,0,0,547,548,
        3,106,53,0,548,550,3,88,44,0,549,551,3,82,41,0,550,549,1,0,0,0,550,
        551,1,0,0,0,551,553,1,0,0,0,552,528,1,0,0,0,552,534,1,0,0,0,552,
        540,1,0,0,0,552,546,1,0,0,0,553,556,1,0,0,0,554,552,1,0,0,0,554,
        555,1,0,0,0,555,89,1,0,0,0,556,554,1,0,0,0,557,558,6,45,-1,0,558,
        582,3,102,51,0,559,582,3,86,43,0,560,582,3,84,42,0,561,562,5,48,
        0,0,562,564,3,90,45,0,563,565,3,82,41,0,564,563,1,0,0,0,564,565,
        1,0,0,0,565,582,1,0,0,0,566,567,3,108,54,0,567,569,3,90,45,0,568,
        570,3,82,41,0,569,568,1,0,0,0,569,570,1,0,0,0,570,582,1,0,0,0,571,
        573,5,36,0,0,572,574,3,2,1,0,573,572,1,0,0,0,573,574,1,0,0,0,574,
        575,1,0,0,0,575,577,3,90,45,0,576,578,3,2,1,0,577,576,1,0,0,0,577,
        578,1,0,0,0,578,579,1,0,0,0,579,580,5,39,0,0,580,582,1,0,0,0,581,
        557,1,0,0,0,581,559,1,0,0,0,581,560,1,0,0,0,581,561,1,0,0,0,581,
        566,1,0,0,0,581,571,1,0,0,0,582,609,1,0,0,0,583,584,10,5,0,0,584,
        585,3,112,56,0,585,587,3,90,45,0,586,588,3,82,41,0,587,586,1,0,0,
        0,587,588,1,0,0,0,588,608,1,0,0,0,589,590,10,4,0,0,590,591,3,114,
        57,0,591,593,3,90,45,0,592,594,3,82,41,0,593,592,1,0,0,0,593,594,
        1,0,0,0,594,608,1,0,0,0,595,596,10,3,0,0,596,597,3,110,55,0,597,
        599,3,90,45,0,598,600,3,82,41,0,599,598,1,0,0,0,599,600,1,0,0,0,
        600,608,1,0,0,0,601,602,10,2,0,0,602,603,3,106,53,0,603,605,3,90,
        45,0,604,606,3,82,41,0,605,604,1,0,0,0,605,606,1,0,0,0,606,608,1,
        0,0,0,607,583,1,0,0,0,607,589,1,0,0,0,607,595,1,0,0,0,607,601,1,
        0,0,0,608,611,1,0,0,0,609,607,1,0,0,0,609,610,1,0,0,0,610,91,1,0,
        0,0,611,609,1,0,0,0,612,613,3,72,36,0,613,93,1,0,0,0,614,616,3,92,
        46,0,615,617,3,98,49,0,616,615,1,0,0,0,616,617,1,0,0,0,617,95,1,
        0,0,0,618,619,3,94,47,0,619,620,5,59,0,0,620,621,7,4,0,0,621,627,
        1,0,0,0,622,623,3,92,46,0,623,624,5,59,0,0,624,625,7,5,0,0,625,627,
        1,0,0,0,626,618,1,0,0,0,626,622,1,0,0,0,627,97,1,0,0,0,628,629,5,
        37,0,0,629,630,3,104,52,0,630,631,5,40,0,0,631,99,1,0,0,0,632,633,
        3,94,47,0,633,634,3,116,58,0,634,635,3,92,46,0,635,101,1,0,0,0,636,
        639,3,100,50,0,637,639,3,96,48,0,638,636,1,0,0,0,638,637,1,0,0,0,
        639,103,1,0,0,0,640,641,3,90,45,0,641,105,1,0,0,0,642,643,7,6,0,
        0,643,107,1,0,0,0,644,645,7,7,0,0,645,109,1,0,0,0,646,647,7,8,0,
        0,647,111,1,0,0,0,648,649,7,9,0,0,649,113,1,0,0,0,650,651,7,10,0,
        0,651,115,1,0,0,0,652,653,7,11,0,0,653,117,1,0,0,0,654,655,5,101,
        0,0,655,656,5,108,0,0,656,119,1,0,0,0,657,658,5,3,0,0,658,663,5,
        102,0,0,659,660,3,2,1,0,660,661,5,7,0,0,661,662,3,122,61,0,662,664,
        1,0,0,0,663,659,1,0,0,0,663,664,1,0,0,0,664,665,1,0,0,0,665,666,
        3,2,1,0,666,667,3,130,65,0,667,668,3,2,1,0,668,672,3,132,66,0,669,
        670,3,2,1,0,670,671,3,134,67,0,671,673,1,0,0,0,672,669,1,0,0,0,672,
        673,1,0,0,0,673,677,1,0,0,0,674,675,3,2,1,0,675,676,3,118,59,0,676,
        678,1,0,0,0,677,674,1,0,0,0,677,678,1,0,0,0,678,121,1,0,0,0,679,
        682,3,124,62,0,680,682,3,126,63,0,681,679,1,0,0,0,681,680,1,0,0,
        0,682,123,1,0,0,0,683,684,5,28,0,0,684,125,1,0,0,0,685,686,3,128,
        64,0,686,687,5,103,0,0,687,127,1,0,0,0,688,693,5,29,0,0,689,690,
        3,2,1,0,690,691,5,30,0,0,691,694,1,0,0,0,692,694,5,42,0,0,693,689,
        1,0,0,0,693,692,1,0,0,0,694,129,1,0,0,0,695,696,5,4,0,0,696,697,
        3,2,1,0,697,698,3,104,52,0,698,131,1,0,0,0,699,703,5,5,0,0,700,701,
        3,2,1,0,701,702,3,138,69,0,702,704,1,0,0,0,703,700,1,0,0,0,704,705,
        1,0,0,0,705,703,1,0,0,0,705,706,1,0,0,0,706,133,1,0,0,0,707,711,
        5,6,0,0,708,709,3,2,1,0,709,710,3,138,69,0,710,712,1,0,0,0,711,708,
        1,0,0,0,712,713,1,0,0,0,713,711,1,0,0,0,713,714,1,0,0,0,714,135,
        1,0,0,0,715,716,3,70,35,0,716,717,3,140,70,0,717,719,3,104,52,0,
        718,720,3,82,41,0,719,718,1,0,0,0,719,720,1,0,0,0,720,728,1,0,0,
        0,721,722,3,104,52,0,722,723,3,142,71,0,723,725,3,70,35,0,724,726,
        3,82,41,0,725,724,1,0,0,0,725,726,1,0,0,0,726,728,1,0,0,0,727,715,
        1,0,0,0,727,721,1,0,0,0,728,137,1,0,0,0,729,730,3,136,68,0,730,139,
        1,0,0,0,731,732,7,12,0,0,732,141,1,0,0,0,733,734,5,47,0,0,734,143,
        1,0,0,0,87,145,150,155,167,175,183,193,198,203,209,221,227,230,238,
        241,257,274,279,283,289,294,301,306,310,315,323,327,332,339,346,
        353,360,369,376,383,386,391,396,401,407,410,420,424,431,445,449,
        453,471,473,493,497,501,509,514,518,522,526,532,538,544,550,552,
        554,564,569,573,577,581,587,593,599,605,607,609,616,626,638,663,
        672,677,681,693,705,713,719,725,727
    ]

class at_krl_parser ( Parser ):

    grammarFileName = "at_krl_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'\\u0423\\u0412\\u0415\\u0420\\u0415\\u041D\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u0422\\u041E\\u0427\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u041F\\u0420\\u0410\\u0412\\u0418\\u041B\\u041E'", 
                     "'\\u0415\\u0421\\u041B\\u0418'", "'\\u0422\\u041E'", 
                     "'\\u0418\\u041D\\u0410\\u0427\\u0415'", "'\\u0422\\u0418\\u041F'", 
                     "'\\u041E\\u0411\\u042A\\u0415\\u041A\\u0422'", "'\\u0413\\u0420\\u0423\\u041F\\u041F\\u0410'", 
                     "'\\u0410\\u0422\\u0420\\u0418\\u0411\\u0423\\u0422'", 
                     "'\\u0410\\u0422\\u0420\\u0418\\u0411\\u0423\\u0422\\u042B'", 
                     "'\\u0417\\u041D\\u0410\\u0427\\u0415\\u041D\\u0418\\u0415'", 
                     "'\\u0418\\u041D\\u0422\\u0415\\u0420\\u0412\\u0410\\u041B'", 
                     "'\\u0418\\u043D\\u0442\\u0435\\u0440\\u0432\\u0430\\u043B'", 
                     "'\\u0421\\u041E\\u0411\\u042B\\u0422\\u0418\\u0415'", 
                     "'\\u0421\\u043E\\u0431\\u044B\\u0442\\u0438\\u0435'", 
                     "'\\u0423\\u0441\\u043B\\u0412\\u043E\\u0437\\u043D'", 
                     "'\\u0423\\u0441\\u043B\\u041D\\u0430\\u0447'", "'\\u0423\\u0441\\u043B\\u041E\\u043A\\u043E\\u043D\\u0447'", 
                     "'\\u0414\\u041B\\u0418\\u0422\\u0415\\u041B\\u042C\\u041D\\u041E\\u0421\\u0422\\u042C'", 
                     "'\\u041A\\u041E\\u041B_\\u0412\\u041E\\u0417\\u041D'", 
                     "'\\u041A\\u041E\\u041B_\\u041D\\u0410\\u0427'", "'\\u041A\\u041E\\u041B_\\u041E\\u041A\\u041E\\u041D\\u0427'", 
                     "'\\u0422\\u0410\\u041A\\u0422_\\u041D\\u0410\\u0427'", 
                     "'\\u0422\\u0410\\u041A\\u0422_\\u041E\\u041A\\u041E\\u041D\\u0427'", 
                     "'\\u0422\\u0410\\u041A\\u0422_\\u0412\\u041E\\u0417\\u041D'", 
                     "'\\u041B\\u043E\\u0433\\u0412\\u044B\\u0440'", "'\\u041E\\u0411\\u042B\\u0427\\u041D\\u041E\\u0415'", 
                     "'\\u041F\\u0415\\u0420\\u0418\\u041E\\u0414\\u0418\\u0427\\u0415\\u0421\\u041A\\u041E\\u0415'", 
                     "'\\u041F\\u0415\\u0420\\u0418\\u041E\\u0414'", "'\\u0421\\u0418\\u041C\\u0412\\u041E\\u041B'", 
                     "'\\u0427\\u0418\\u0421\\u041B\\u041E'", "'\\u041D\\u0415\\u0427\\u0415\\u0422\\u041A\\u0418\\u0419'", 
                     "'\\u041E\\u0422'", "'\\u0414\\u041E'", "'('", "'['", 
                     "'{'", "')'", "']'", "'}'", "':'", "','", "';'", "'+'", 
                     "'<-'", "'->'", "'-'", "'*'", "'/'", "'||'", "'|'", 
                     "'&&'", "'&'", "'<'", "'>'", "':='", "'='", "'.'", 
                     "'%'", "'`'", "'=='", "'<>'", "'!='", "'<='", "'>='", 
                     "'~'", "'^'", "'**'", "'and'", "'or'", "'xor'", "'not'", 
                     "'mod'", "'div'", "'add'", "'sub'", "'mul'", "'pow'", 
                     "'eq'", "'lt'", "'gt'", "'le'", "'ge'", "'ne'", "'!'", 
                     "'b'", "'bi'", "'m'", "'mi'", "'s'", "'si'", "'f'", 
                     "'fi'", "'d'", "'di'", "'o'", "'oi'", "'e'", "'a'", 
                     "'\\u041A\\u041E\\u041C\\u041C\\u0415\\u041D\\u0422\\u0410\\u0420\\u0418\\u0419'" ]

    symbolicNames = [ "<INVALID>", "BELIEF", "ACCURACY", "RULE", "IF", "THEN", 
                      "ELSE", "TYPE", "OBJECT", "GROUP", "ATTR", "ATTRS", 
                      "VALUE", "INTERVAL", "CASED_INTERVAL", "EVENT", "CASED_EVENT", 
                      "OCCURANCE_CONDITION", "OPEN", "CLOSE", "DURATION", 
                      "OCCURANCE_COUNT", "OPEN_COUNT", "CLOSE_COUNT", "OPEN_TACT", 
                      "CLOSE_TACT", "OCCURANCE_TACT", "SIMPLE_EXP_TYPE", 
                      "SIMPLE", "PERIODIC", "PERIOD", "SYM", "NUM", "FUZ", 
                      "FROM", "TO", "LPAR", "LSQB", "LBRACE", "RPAR", "RSQB", 
                      "RBRACE", "COLON", "COMMA", "SEMI", "PLUS", "LEFT_ASSIGN", 
                      "RIGHT_ASSIGN", "MINUS", "STAR", "SLASH", "DOUBLEVBAR", 
                      "VBAR", "DOUBLEAMPER", "AMPER", "LESS", "GREATER", 
                      "COLON_EQ", "EQUAL", "DOT", "PERCENT", "BACKQUOTE", 
                      "EQEQUAL", "INEQUAL", "NOTEQUAL", "LESSEQUAL", "GREATEREQUAL", 
                      "TILDE", "CIRCUMFLEX", "DOUBLESTAR", "AND", "OR", 
                      "XOR", "NOT", "MOD", "DIV", "ADD", "SUB", "MUL", "POW", 
                      "EQ", "LT", "GT", "LE", "GE", "NE", "EXCL", "ALLEN_B", 
                      "ALLEN_BI", "ALLEN_M", "ALLEN_MI", "ALLEN_S", "ALLEN_SI", 
                      "ALLEN_F", "ALLEN_FI", "ALLEN_D", "ALLEN_DI", "ALLEN_O", 
                      "ALLEN_OI", "ALLEN_E", "ALLEN_A", "COMMENT", "NAME", 
                      "NUMBER", "STRING", "LANG_COMMENT", "WS", "NEWLINE", 
                      "COMMENT_DATA" ]

    RULE_lang_comment = 0
    RULE_newline = 1
    RULE_knowledge_base = 2
    RULE_kb_types = 3
    RULE_kb_classes = 4
    RULE_kb_rules = 5
    RULE_kb_type = 6
    RULE_kb_type_body = 7
    RULE_fuzzy_type_body = 8
    RULE_membership_function = 9
    RULE_membership_functions = 10
    RULE_mf_def = 11
    RULE_mf_body = 12
    RULE_mf_point = 13
    RULE_symbolic_type_body = 14
    RULE_symbolic_type_values = 15
    RULE_numeric_type_body = 16
    RULE_kb_class = 17
    RULE_kb_class_body = 18
    RULE_object_body = 19
    RULE_attributes = 20
    RULE_attribute = 21
    RULE_short_attribute = 22
    RULE_long_attribute = 23
    RULE_event_body = 24
    RULE_occurance_condition = 25
    RULE_interval_body = 26
    RULE_open = 27
    RULE_close = 28
    RULE_occurance_condition_declaration = 29
    RULE_open_declaration = 30
    RULE_close_declaration = 31
    RULE_attr_declaration = 32
    RULE_temporal_attribute_condition = 33
    RULE_simple_value = 34
    RULE_ref_path = 35
    RULE_simple_ref = 36
    RULE_simple_operation = 37
    RULE_simple_evaluatable = 38
    RULE_belief = 39
    RULE_accuracy = 40
    RULE_non_factor = 41
    RULE_kb_value = 42
    RULE_kb_reference = 43
    RULE_kb_operation = 44
    RULE_kb_evaluatable = 45
    RULE_allen_reference = 46
    RULE_allen_indexed_reference = 47
    RULE_allen_attribute_expression = 48
    RULE_index = 49
    RULE_allen_operation = 50
    RULE_allen_evaluatable = 51
    RULE_evaluatable = 52
    RULE_logical_binary = 53
    RULE_logical_unary = 54
    RULE_compare = 55
    RULE_high_p_math = 56
    RULE_low_p_math = 57
    RULE_allen = 58
    RULE_commentary = 59
    RULE_kb_rule = 60
    RULE_rule_type = 61
    RULE_rule_simple_type = 62
    RULE_rule_periodic_type = 63
    RULE_rule_periodic_type_def = 64
    RULE_kb_rule_condition = 65
    RULE_kb_rule_instructions = 66
    RULE_kb_rule_else_instructions = 67
    RULE_assign_instruction = 68
    RULE_instruction = 69
    RULE_left_assign = 70
    RULE_right_assign = 71

    ruleNames =  [ "lang_comment", "newline", "knowledge_base", "kb_types", 
                   "kb_classes", "kb_rules", "kb_type", "kb_type_body", 
                   "fuzzy_type_body", "membership_function", "membership_functions", 
                   "mf_def", "mf_body", "mf_point", "symbolic_type_body", 
                   "symbolic_type_values", "numeric_type_body", "kb_class", 
                   "kb_class_body", "object_body", "attributes", "attribute", 
                   "short_attribute", "long_attribute", "event_body", "occurance_condition", 
                   "interval_body", "open", "close", "occurance_condition_declaration", 
                   "open_declaration", "close_declaration", "attr_declaration", 
                   "temporal_attribute_condition", "simple_value", "ref_path", 
                   "simple_ref", "simple_operation", "simple_evaluatable", 
                   "belief", "accuracy", "non_factor", "kb_value", "kb_reference", 
                   "kb_operation", "kb_evaluatable", "allen_reference", 
                   "allen_indexed_reference", "allen_attribute_expression", 
                   "index", "allen_operation", "allen_evaluatable", "evaluatable", 
                   "logical_binary", "logical_unary", "compare", "high_p_math", 
                   "low_p_math", "allen", "commentary", "kb_rule", "rule_type", 
                   "rule_simple_type", "rule_periodic_type", "rule_periodic_type_def", 
                   "kb_rule_condition", "kb_rule_instructions", "kb_rule_else_instructions", 
                   "assign_instruction", "instruction", "left_assign", "right_assign" ]

    EOF = Token.EOF
    BELIEF=1
    ACCURACY=2
    RULE=3
    IF=4
    THEN=5
    ELSE=6
    TYPE=7
    OBJECT=8
    GROUP=9
    ATTR=10
    ATTRS=11
    VALUE=12
    INTERVAL=13
    CASED_INTERVAL=14
    EVENT=15
    CASED_EVENT=16
    OCCURANCE_CONDITION=17
    OPEN=18
    CLOSE=19
    DURATION=20
    OCCURANCE_COUNT=21
    OPEN_COUNT=22
    CLOSE_COUNT=23
    OPEN_TACT=24
    CLOSE_TACT=25
    OCCURANCE_TACT=26
    SIMPLE_EXP_TYPE=27
    SIMPLE=28
    PERIODIC=29
    PERIOD=30
    SYM=31
    NUM=32
    FUZ=33
    FROM=34
    TO=35
    LPAR=36
    LSQB=37
    LBRACE=38
    RPAR=39
    RSQB=40
    RBRACE=41
    COLON=42
    COMMA=43
    SEMI=44
    PLUS=45
    LEFT_ASSIGN=46
    RIGHT_ASSIGN=47
    MINUS=48
    STAR=49
    SLASH=50
    DOUBLEVBAR=51
    VBAR=52
    DOUBLEAMPER=53
    AMPER=54
    LESS=55
    GREATER=56
    COLON_EQ=57
    EQUAL=58
    DOT=59
    PERCENT=60
    BACKQUOTE=61
    EQEQUAL=62
    INEQUAL=63
    NOTEQUAL=64
    LESSEQUAL=65
    GREATEREQUAL=66
    TILDE=67
    CIRCUMFLEX=68
    DOUBLESTAR=69
    AND=70
    OR=71
    XOR=72
    NOT=73
    MOD=74
    DIV=75
    ADD=76
    SUB=77
    MUL=78
    POW=79
    EQ=80
    LT=81
    GT=82
    LE=83
    GE=84
    NE=85
    EXCL=86
    ALLEN_B=87
    ALLEN_BI=88
    ALLEN_M=89
    ALLEN_MI=90
    ALLEN_S=91
    ALLEN_SI=92
    ALLEN_F=93
    ALLEN_FI=94
    ALLEN_D=95
    ALLEN_DI=96
    ALLEN_O=97
    ALLEN_OI=98
    ALLEN_E=99
    ALLEN_A=100
    COMMENT=101
    NAME=102
    NUMBER=103
    STRING=104
    LANG_COMMENT=105
    WS=106
    NEWLINE=107
    COMMENT_DATA=108

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Lang_commentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LANG_COMMENT(self):
            return self.getToken(at_krl_parser.LANG_COMMENT, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_lang_comment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLang_comment" ):
                listener.enterLang_comment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLang_comment" ):
                listener.exitLang_comment(self)




    def lang_comment(self):

        localctx = at_krl_parser.Lang_commentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_lang_comment)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==105:
                self.state = 144
                self.match(at_krl_parser.LANG_COMMENT)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NewlineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.NEWLINE)
            else:
                return self.getToken(at_krl_parser.NEWLINE, i)

        def getRuleIndex(self):
            return at_krl_parser.RULE_newline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNewline" ):
                listener.enterNewline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNewline" ):
                listener.exitNewline(self)




    def newline(self):

        localctx = at_krl_parser.NewlineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_newline)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 148 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 147
                    self.match(at_krl_parser.NEWLINE)

                else:
                    raise NoViableAltException(self)
                self.state = 150 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Knowledge_baseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_types(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_typesContext,0)


        def kb_classes(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_classesContext,0)


        def kb_rules(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_rulesContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_knowledge_base

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnowledge_base" ):
                listener.enterKnowledge_base(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnowledge_base" ):
                listener.exitKnowledge_base(self)




    def knowledge_base(self):

        localctx = at_krl_parser.Knowledge_baseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_knowledge_base)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 152
                    self.newline() 
                self.state = 157
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

            self.state = 158
            self.kb_types()
            self.state = 159
            self.kb_classes()
            self.state = 160
            self.kb_rules()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_typesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Kb_typeContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Kb_typeContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_types

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_types" ):
                listener.enterKb_types(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_types" ):
                listener.exitKb_types(self)




    def kb_types(self):

        localctx = at_krl_parser.Kb_typesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_kb_types)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 162
                    self.kb_type()
                    self.state = 163
                    self.newline() 
                self.state = 169
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_classesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_class(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Kb_classContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Kb_classContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_classes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_classes" ):
                listener.enterKb_classes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_classes" ):
                listener.exitKb_classes(self)




    def kb_classes(self):

        localctx = at_krl_parser.Kb_classesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_kb_classes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 170
                    self.kb_class()
                    self.state = 171
                    self.newline() 
                self.state = 177
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rulesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_rule(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Kb_ruleContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Kb_ruleContext,i)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_rules

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rules" ):
                listener.enterKb_rules(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rules" ):
                listener.exitKb_rules(self)




    def kb_rules(self):

        localctx = at_krl_parser.Kb_rulesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_kb_rules)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 183
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 178
                    self.kb_rule()
                    self.state = 179
                    self.newline() 
                self.state = 185
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(at_krl_parser.TYPE, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def kb_type_body(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_type_bodyContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_type" ):
                listener.enterKb_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_type" ):
                listener.exitKb_type(self)




    def kb_type(self):

        localctx = at_krl_parser.Kb_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_kb_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.match(at_krl_parser.TYPE)
            self.state = 187
            self.match(at_krl_parser.NAME)
            self.state = 188
            self.newline()
            self.state = 189
            self.kb_type_body()
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 190
                self.newline()
                self.state = 191
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numeric_type_body(self):
            return self.getTypedRuleContext(at_krl_parser.Numeric_type_bodyContext,0)


        def symbolic_type_body(self):
            return self.getTypedRuleContext(at_krl_parser.Symbolic_type_bodyContext,0)


        def fuzzy_type_body(self):
            return self.getTypedRuleContext(at_krl_parser.Fuzzy_type_bodyContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_type_body" ):
                listener.enterKb_type_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_type_body" ):
                listener.exitKb_type_body(self)




    def kb_type_body(self):

        localctx = at_krl_parser.Kb_type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_kb_type_body)
        try:
            self.state = 198
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                self.numeric_type_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 196
                self.symbolic_type_body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 197
                self.fuzzy_type_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Fuzzy_type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUZ(self):
            return self.getToken(at_krl_parser.FUZ, 0)

        def membership_functions(self):
            return self.getTypedRuleContext(at_krl_parser.Membership_functionsContext,0)


        def symbolic_type_body(self):
            return self.getTypedRuleContext(at_krl_parser.Symbolic_type_bodyContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def NUMBER(self):
            return self.getToken(at_krl_parser.NUMBER, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_fuzzy_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuzzy_type_body" ):
                listener.enterFuzzy_type_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuzzy_type_body" ):
                listener.exitFuzzy_type_body(self)




    def fuzzy_type_body(self):

        localctx = at_krl_parser.Fuzzy_type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_fuzzy_type_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==31:
                self.state = 200
                self.symbolic_type_body()
                self.state = 201
                self.newline()


            self.state = 205
            self.match(at_krl_parser.FUZ)
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 206
                self.newline()
                self.state = 207
                self.match(at_krl_parser.NUMBER)


            self.state = 211
            self.membership_functions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Membership_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mf_def(self):
            return self.getTypedRuleContext(at_krl_parser.Mf_defContext,0)


        def mf_body(self):
            return self.getTypedRuleContext(at_krl_parser.Mf_bodyContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_membership_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembership_function" ):
                listener.enterMembership_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembership_function" ):
                listener.exitMembership_function(self)




    def membership_function(self):

        localctx = at_krl_parser.Membership_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_membership_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.mf_def()
            self.state = 214
            self.mf_body()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Membership_functionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def membership_function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Membership_functionContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Membership_functionContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_membership_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembership_functions" ):
                listener.enterMembership_functions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembership_functions" ):
                listener.exitMembership_functions(self)




    def membership_functions(self):

        localctx = at_krl_parser.Membership_functionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_membership_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 216
                    self.newline()
                    self.state = 217
                    self.membership_function()

                else:
                    raise NoViableAltException(self)
                self.state = 221 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mf_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(at_krl_parser.STRING, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.NUMBER)
            else:
                return self.getToken(at_krl_parser.NUMBER, i)

        def EQUAL(self):
            return self.getToken(at_krl_parser.EQUAL, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_mf_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMf_def" ):
                listener.enterMf_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMf_def" ):
                listener.exitMf_def(self)




    def mf_def(self):

        localctx = at_krl_parser.Mf_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_mf_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(at_krl_parser.STRING)
            self.state = 224
            self.match(at_krl_parser.NUMBER)
            self.state = 225
            self.match(at_krl_parser.NUMBER)
            self.state = 227
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==103:
                self.state = 226
                self.match(at_krl_parser.NUMBER)


            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 229
                self.match(at_krl_parser.EQUAL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mf_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(at_krl_parser.LBRACE, 0)

        def mf_point(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Mf_pointContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Mf_pointContext,i)


        def RBRACE(self):
            return self.getToken(at_krl_parser.RBRACE, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.SEMI)
            else:
                return self.getToken(at_krl_parser.SEMI, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.COMMA)
            else:
                return self.getToken(at_krl_parser.COMMA, i)

        def getRuleIndex(self):
            return at_krl_parser.RULE_mf_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMf_body" ):
                listener.enterMf_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMf_body" ):
                listener.exitMf_body(self)




    def mf_body(self):

        localctx = at_krl_parser.Mf_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_mf_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(at_krl_parser.LBRACE)
            self.state = 233
            self.mf_point()
            self.state = 236 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 234
                    _la = self._input.LA(1)
                    if not(_la==43 or _la==44):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 235
                    self.mf_point()

                else:
                    raise NoViableAltException(self)
                self.state = 238 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

            self.state = 241
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43 or _la==44:
                self.state = 240
                _la = self._input.LA(1)
                if not(_la==43 or _la==44):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 243
            self.match(at_krl_parser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Mf_pointContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.NUMBER)
            else:
                return self.getToken(at_krl_parser.NUMBER, i)

        def VBAR(self):
            return self.getToken(at_krl_parser.VBAR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_mf_point

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMf_point" ):
                listener.enterMf_point(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMf_point" ):
                listener.exitMf_point(self)




    def mf_point(self):

        localctx = at_krl_parser.Mf_pointContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_mf_point)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(at_krl_parser.NUMBER)
            self.state = 246
            self.match(at_krl_parser.VBAR)
            self.state = 247
            self.match(at_krl_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Symbolic_type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SYM(self):
            return self.getToken(at_krl_parser.SYM, 0)

        def symbolic_type_values(self):
            return self.getTypedRuleContext(at_krl_parser.Symbolic_type_valuesContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_symbolic_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolic_type_body" ):
                listener.enterSymbolic_type_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolic_type_body" ):
                listener.exitSymbolic_type_body(self)




    def symbolic_type_body(self):

        localctx = at_krl_parser.Symbolic_type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_symbolic_type_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.match(at_krl_parser.SYM)
            self.state = 250
            self.symbolic_type_values()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Symbolic_type_valuesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.STRING)
            else:
                return self.getToken(at_krl_parser.STRING, i)

        def getRuleIndex(self):
            return at_krl_parser.RULE_symbolic_type_values

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSymbolic_type_values" ):
                listener.enterSymbolic_type_values(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSymbolic_type_values" ):
                listener.exitSymbolic_type_values(self)




    def symbolic_type_values(self):

        localctx = at_krl_parser.Symbolic_type_valuesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_symbolic_type_values)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 255 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 252
                    self.newline()
                    self.state = 253
                    self.match(at_krl_parser.STRING)

                else:
                    raise NoViableAltException(self)
                self.state = 257 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,15,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Numeric_type_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(at_krl_parser.NUM, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def FROM(self):
            return self.getToken(at_krl_parser.FROM, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.NUMBER)
            else:
                return self.getToken(at_krl_parser.NUMBER, i)

        def TO(self):
            return self.getToken(at_krl_parser.TO, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_numeric_type_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumeric_type_body" ):
                listener.enterNumeric_type_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumeric_type_body" ):
                listener.exitNumeric_type_body(self)




    def numeric_type_body(self):

        localctx = at_krl_parser.Numeric_type_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_numeric_type_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 259
            self.match(at_krl_parser.NUM)
            self.state = 260
            self.newline()
            self.state = 261
            self.match(at_krl_parser.FROM)
            self.state = 262
            self.match(at_krl_parser.NUMBER)
            self.state = 263
            self.newline()
            self.state = 264
            self.match(at_krl_parser.TO)
            self.state = 265
            self.match(at_krl_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_classContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OBJECT(self):
            return self.getToken(at_krl_parser.OBJECT, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def kb_class_body(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_class_bodyContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_class

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_class" ):
                listener.enterKb_class(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_class" ):
                listener.exitKb_class(self)




    def kb_class(self):

        localctx = at_krl_parser.Kb_classContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_kb_class)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 267
            self.match(at_krl_parser.OBJECT)
            self.state = 268
            self.match(at_krl_parser.NAME)
            self.state = 269
            self.newline()
            self.state = 270
            self.kb_class_body()
            self.state = 274
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 271
                self.newline()
                self.state = 272
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_class_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_body(self):
            return self.getTypedRuleContext(at_krl_parser.Object_bodyContext,0)


        def event_body(self):
            return self.getTypedRuleContext(at_krl_parser.Event_bodyContext,0)


        def interval_body(self):
            return self.getTypedRuleContext(at_krl_parser.Interval_bodyContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_class_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_class_body" ):
                listener.enterKb_class_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_class_body" ):
                listener.exitKb_class_body(self)




    def kb_class_body(self):

        localctx = at_krl_parser.Kb_class_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_kb_class_body)
        try:
            self.state = 279
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
                self.object_body()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 277
                self.event_body()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.interval_body()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Object_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attributes(self):
            return self.getTypedRuleContext(at_krl_parser.AttributesContext,0)


        def GROUP(self):
            return self.getToken(at_krl_parser.GROUP, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_object_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterObject_body" ):
                listener.enterObject_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitObject_body" ):
                listener.exitObject_body(self)




    def object_body(self):

        localctx = at_krl_parser.Object_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_object_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 283
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 281
                self.match(at_krl_parser.GROUP)
                self.state = 282
                self.match(at_krl_parser.NAME)


            self.state = 285
            self.attributes()
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.state = 286
                self.newline()
                self.state = 287
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def ATTRS(self):
            return self.getToken(at_krl_parser.ATTRS, 0)

        def attribute(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.AttributeContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.AttributeContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_attributes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttributes" ):
                listener.enterAttributes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttributes" ):
                listener.exitAttributes(self)




    def attributes(self):

        localctx = at_krl_parser.AttributesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_attributes)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.state = 291
                self.newline()
                self.state = 292
                self.match(at_krl_parser.ATTRS)


            self.state = 299 
            self._errHandler.sync(self)
            _alt = 1+1
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1+1:
                    self.state = 296
                    self.newline()
                    self.state = 297
                    self.attribute()

                else:
                    raise NoViableAltException(self)
                self.state = 301 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_declaration(self):
            return self.getTypedRuleContext(at_krl_parser.Attr_declarationContext,0)


        def long_attribute(self):
            return self.getTypedRuleContext(at_krl_parser.Long_attributeContext,0)


        def short_attribute(self):
            return self.getTypedRuleContext(at_krl_parser.Short_attributeContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttribute" ):
                listener.enterAttribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttribute" ):
                listener.exitAttribute(self)




    def attribute(self):

        localctx = at_krl_parser.AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_attribute)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.attr_declaration()
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [107]:
                self.state = 304
                self.long_attribute()
                pass
            elif token in [42]:
                self.state = 305
                self.short_attribute()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Short_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COLON(self):
            return self.getToken(at_krl_parser.COLON, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def TYPE(self):
            return self.getToken(at_krl_parser.TYPE, 0)

        def EQUAL(self):
            return self.getToken(at_krl_parser.EQUAL, 0)

        def kb_operation(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_operationContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_short_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterShort_attribute" ):
                listener.enterShort_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitShort_attribute" ):
                listener.exitShort_attribute(self)




    def short_attribute(self):

        localctx = at_krl_parser.Short_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_short_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.match(at_krl_parser.COLON)
            self.state = 310
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 309
                self.match(at_krl_parser.TYPE)


            self.state = 312
            self.match(at_krl_parser.NAME)
            self.state = 315
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 313
                self.match(at_krl_parser.EQUAL)
                self.state = 314
                self.kb_operation(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Long_attributeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def TYPE(self):
            return self.getToken(at_krl_parser.TYPE, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def VALUE(self):
            return self.getToken(at_krl_parser.VALUE, 0)

        def kb_operation(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_operationContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_long_attribute

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLong_attribute" ):
                listener.enterLong_attribute(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLong_attribute" ):
                listener.exitLong_attribute(self)




    def long_attribute(self):

        localctx = at_krl_parser.Long_attributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_long_attribute)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 317
            self.newline()
            self.state = 318
            self.match(at_krl_parser.TYPE)
            self.state = 319
            self.match(at_krl_parser.NAME)
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 320
                self.newline()
                self.state = 321
                self.match(at_krl_parser.VALUE)
                self.state = 323
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 322
                    self.newline()


                self.state = 325
                self.kb_operation(0)


            self.state = 332
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.state = 329
                self.newline()
                self.state = 330
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Event_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(at_krl_parser.GROUP, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def occurance_condition(self):
            return self.getTypedRuleContext(at_krl_parser.Occurance_conditionContext,0)


        def EVENT(self):
            return self.getToken(at_krl_parser.EVENT, 0)

        def CASED_EVENT(self):
            return self.getToken(at_krl_parser.CASED_EVENT, 0)

        def ATTRS(self):
            return self.getToken(at_krl_parser.ATTRS, 0)

        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_event_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvent_body" ):
                listener.enterEvent_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvent_body" ):
                listener.exitEvent_body(self)




    def event_body(self):

        localctx = at_krl_parser.Event_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_event_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 334
            self.match(at_krl_parser.GROUP)
            self.state = 335
            _la = self._input.LA(1)
            if not(_la==15 or _la==16):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 339
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.state = 336
                self.newline()
                self.state = 337
                self.match(at_krl_parser.ATTRS)


            self.state = 341
            self.newline()
            self.state = 342
            self.occurance_condition()
            self.state = 346
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.state = 343
                self.newline()
                self.state = 344
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Occurance_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def occurance_condition_declaration(self):
            return self.getTypedRuleContext(at_krl_parser.Occurance_condition_declarationContext,0)


        def temporal_attribute_condition(self):
            return self.getTypedRuleContext(at_krl_parser.Temporal_attribute_conditionContext,0)


        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_occurance_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOccurance_condition" ):
                listener.enterOccurance_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOccurance_condition" ):
                listener.exitOccurance_condition(self)




    def occurance_condition(self):

        localctx = at_krl_parser.Occurance_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_occurance_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 348
            self.occurance_condition_declaration()
            self.state = 349
            self.temporal_attribute_condition()
            self.state = 353
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.state = 350
                self.newline()
                self.state = 351
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Interval_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(at_krl_parser.GROUP, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def open_(self):
            return self.getTypedRuleContext(at_krl_parser.OpenContext,0)


        def close(self):
            return self.getTypedRuleContext(at_krl_parser.CloseContext,0)


        def INTERVAL(self):
            return self.getToken(at_krl_parser.INTERVAL, 0)

        def CASED_INTERVAL(self):
            return self.getToken(at_krl_parser.CASED_INTERVAL, 0)

        def ATTRS(self):
            return self.getToken(at_krl_parser.ATTRS, 0)

        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_interval_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterval_body" ):
                listener.enterInterval_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterval_body" ):
                listener.exitInterval_body(self)




    def interval_body(self):

        localctx = at_krl_parser.Interval_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_interval_body)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 355
            self.match(at_krl_parser.GROUP)
            self.state = 356
            _la = self._input.LA(1)
            if not(_la==13 or _la==14):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.state = 357
                self.newline()
                self.state = 358
                self.match(at_krl_parser.ATTRS)


            self.state = 362
            self.newline()
            self.state = 363
            self.open_()
            self.state = 364
            self.newline()
            self.state = 365
            self.close()
            self.state = 369
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.state = 366
                self.newline()
                self.state = 367
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def open_declaration(self):
            return self.getTypedRuleContext(at_krl_parser.Open_declarationContext,0)


        def temporal_attribute_condition(self):
            return self.getTypedRuleContext(at_krl_parser.Temporal_attribute_conditionContext,0)


        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_open

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen" ):
                listener.enterOpen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen" ):
                listener.exitOpen(self)




    def open_(self):

        localctx = at_krl_parser.OpenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_open)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 371
            self.open_declaration()
            self.state = 372
            self.temporal_attribute_condition()
            self.state = 376
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 373
                self.newline()
                self.state = 374
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CloseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def close_declaration(self):
            return self.getTypedRuleContext(at_krl_parser.Close_declarationContext,0)


        def temporal_attribute_condition(self):
            return self.getTypedRuleContext(at_krl_parser.Temporal_attribute_conditionContext,0)


        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_close

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose" ):
                listener.enterClose(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose" ):
                listener.exitClose(self)




    def close(self):

        localctx = at_krl_parser.CloseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_close)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.close_declaration()
            self.state = 379
            self.temporal_attribute_condition()
            self.state = 383
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.state = 380
                self.newline()
                self.state = 381
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Occurance_condition_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OCCURANCE_CONDITION(self):
            return self.getToken(at_krl_parser.OCCURANCE_CONDITION, 0)

        def ATTR(self):
            return self.getToken(at_krl_parser.ATTR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_occurance_condition_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOccurance_condition_declaration" ):
                listener.enterOccurance_condition_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOccurance_condition_declaration" ):
                listener.exitOccurance_condition_declaration(self)




    def occurance_condition_declaration(self):

        localctx = at_krl_parser.Occurance_condition_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_occurance_condition_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 386
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 385
                self.match(at_krl_parser.ATTR)


            self.state = 388
            self.match(at_krl_parser.OCCURANCE_CONDITION)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Open_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN(self):
            return self.getToken(at_krl_parser.OPEN, 0)

        def ATTR(self):
            return self.getToken(at_krl_parser.ATTR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_open_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpen_declaration" ):
                listener.enterOpen_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpen_declaration" ):
                listener.exitOpen_declaration(self)




    def open_declaration(self):

        localctx = at_krl_parser.Open_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_open_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 390
                self.match(at_krl_parser.ATTR)


            self.state = 393
            self.match(at_krl_parser.OPEN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Close_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLOSE(self):
            return self.getToken(at_krl_parser.CLOSE, 0)

        def ATTR(self):
            return self.getToken(at_krl_parser.ATTR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_close_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClose_declaration" ):
                listener.enterClose_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClose_declaration" ):
                listener.exitClose_declaration(self)




    def close_declaration(self):

        localctx = at_krl_parser.Close_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_close_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 396
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 395
                self.match(at_krl_parser.ATTR)


            self.state = 398
            self.match(at_krl_parser.CLOSE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Attr_declarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def ATTR(self):
            return self.getToken(at_krl_parser.ATTR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_attr_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr_declaration" ):
                listener.enterAttr_declaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr_declaration" ):
                listener.exitAttr_declaration(self)




    def attr_declaration(self):

        localctx = at_krl_parser.Attr_declarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_attr_declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 400
                self.match(at_krl_parser.ATTR)


            self.state = 403
            self.match(at_krl_parser.NAME)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Temporal_attribute_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(at_krl_parser.EQUAL, 0)

        def simple_evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_evaluatableContext,0)


        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def TYPE(self):
            return self.getToken(at_krl_parser.TYPE, 0)

        def SIMPLE_EXP_TYPE(self):
            return self.getToken(at_krl_parser.SIMPLE_EXP_TYPE, 0)

        def VALUE(self):
            return self.getToken(at_krl_parser.VALUE, 0)

        def COLON(self):
            return self.getToken(at_krl_parser.COLON, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_temporal_attribute_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTemporal_attribute_condition" ):
                listener.enterTemporal_attribute_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTemporal_attribute_condition" ):
                listener.exitTemporal_attribute_condition(self)




    def temporal_attribute_condition(self):

        localctx = at_krl_parser.Temporal_attribute_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_temporal_attribute_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 424
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [42, 58]:
                self.state = 410
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==42:
                    self.state = 405
                    self.match(at_krl_parser.COLON)
                    self.state = 407
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==7:
                        self.state = 406
                        self.match(at_krl_parser.TYPE)


                    self.state = 409
                    self.match(at_krl_parser.SIMPLE_EXP_TYPE)


                self.state = 412
                self.match(at_krl_parser.EQUAL)
                self.state = 413
                self.simple_evaluatable()
                pass
            elif token in [107]:
                self.state = 414
                self.newline()
                self.state = 415
                self.match(at_krl_parser.TYPE)
                self.state = 416
                self.match(at_krl_parser.SIMPLE_EXP_TYPE)
                self.state = 417
                self.newline()
                self.state = 418
                self.match(at_krl_parser.VALUE)
                self.state = 420
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 419
                    self.newline()


                self.state = 422
                self.simple_evaluatable()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(at_krl_parser.STRING, 0)

        def NUMBER(self):
            return self.getToken(at_krl_parser.NUMBER, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_simple_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_value" ):
                listener.enterSimple_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_value" ):
                listener.exitSimple_value(self)




    def simple_value(self):

        localctx = at_krl_parser.Simple_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_simple_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            _la = self._input.LA(1)
            if not(_la==103 or _la==104):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Ref_pathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def DOT(self):
            return self.getToken(at_krl_parser.DOT, 0)

        def ref_path(self):
            return self.getTypedRuleContext(at_krl_parser.Ref_pathContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_ref_path

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRef_path" ):
                listener.enterRef_path(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRef_path" ):
                listener.exitRef_path(self)




    def ref_path(self):

        localctx = at_krl_parser.Ref_pathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_ref_path)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 428
            self.match(at_krl_parser.NAME)
            self.state = 431
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,43,self._ctx)
            if la_ == 1:
                self.state = 429
                self.match(at_krl_parser.DOT)
                self.state = 430
                self.ref_path()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_refContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ref_path(self):
            return self.getTypedRuleContext(at_krl_parser.Ref_pathContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_simple_ref

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_ref" ):
                listener.enterSimple_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_ref" ):
                listener.exitSimple_ref(self)




    def simple_ref(self):

        localctx = at_krl_parser.Simple_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_simple_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            self.ref_path()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Simple_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_ref(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_refContext,0)


        def simple_value(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_valueContext,0)


        def logical_unary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_unaryContext,0)


        def simple_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Simple_operationContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Simple_operationContext,i)


        def MINUS(self):
            return self.getToken(at_krl_parser.MINUS, 0)

        def LPAR(self):
            return self.getToken(at_krl_parser.LPAR, 0)

        def RPAR(self):
            return self.getToken(at_krl_parser.RPAR, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def high_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.High_p_mathContext,0)


        def low_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.Low_p_mathContext,0)


        def compare(self):
            return self.getTypedRuleContext(at_krl_parser.CompareContext,0)


        def logical_binary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_binaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_simple_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_operation" ):
                listener.enterSimple_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_operation" ):
                listener.exitSimple_operation(self)



    def simple_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = at_krl_parser.Simple_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_simple_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 453
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [102]:
                self.state = 436
                self.simple_ref()
                pass
            elif token in [103, 104]:
                self.state = 437
                self.simple_value()
                pass
            elif token in [67, 73, 86]:
                self.state = 438
                self.logical_unary()
                self.state = 439
                self.simple_operation(7)
                pass
            elif token in [48]:
                self.state = 441
                self.match(at_krl_parser.MINUS)
                self.state = 442
                self.simple_operation(2)
                pass
            elif token in [36]:
                self.state = 443
                self.match(at_krl_parser.LPAR)
                self.state = 445
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 444
                    self.newline()


                self.state = 447
                self.simple_operation(0)
                self.state = 449
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 448
                    self.newline()


                self.state = 451
                self.match(at_krl_parser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 473
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 471
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
                    if la_ == 1:
                        localctx = at_krl_parser.Simple_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_operation)
                        self.state = 455
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 456
                        self.high_p_math()
                        self.state = 457
                        self.simple_operation(7)
                        pass

                    elif la_ == 2:
                        localctx = at_krl_parser.Simple_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_operation)
                        self.state = 459
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 460
                        self.low_p_math()
                        self.state = 461
                        self.simple_operation(6)
                        pass

                    elif la_ == 3:
                        localctx = at_krl_parser.Simple_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_operation)
                        self.state = 463
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 464
                        self.compare()
                        self.state = 465
                        self.simple_operation(5)
                        pass

                    elif la_ == 4:
                        localctx = at_krl_parser.Simple_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_simple_operation)
                        self.state = 467
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 468
                        self.logical_binary()
                        self.state = 469
                        self.simple_operation(4)
                        pass

             
                self.state = 475
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Simple_evaluatableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_operation(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_operationContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_simple_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_evaluatable" ):
                listener.enterSimple_evaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_evaluatable" ):
                listener.exitSimple_evaluatable(self)




    def simple_evaluatable(self):

        localctx = at_krl_parser.Simple_evaluatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_simple_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.simple_operation(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeliefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BELIEF(self):
            return self.getToken(at_krl_parser.BELIEF, 0)

        def LSQB(self):
            return self.getToken(at_krl_parser.LSQB, 0)

        def NUMBER(self, i:int=None):
            if i is None:
                return self.getTokens(at_krl_parser.NUMBER)
            else:
                return self.getToken(at_krl_parser.NUMBER, i)

        def RSQB(self):
            return self.getToken(at_krl_parser.RSQB, 0)

        def SEMI(self):
            return self.getToken(at_krl_parser.SEMI, 0)

        def COMMA(self):
            return self.getToken(at_krl_parser.COMMA, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_belief

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBelief" ):
                listener.enterBelief(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBelief" ):
                listener.exitBelief(self)




    def belief(self):

        localctx = at_krl_parser.BeliefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_belief)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 478
            self.match(at_krl_parser.BELIEF)
            self.state = 479
            self.match(at_krl_parser.LSQB)
            self.state = 480
            self.match(at_krl_parser.NUMBER)
            self.state = 481
            _la = self._input.LA(1)
            if not(_la==43 or _la==44):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 482
            self.match(at_krl_parser.NUMBER)
            self.state = 483
            self.match(at_krl_parser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccuracyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ACCURACY(self):
            return self.getToken(at_krl_parser.ACCURACY, 0)

        def NUMBER(self):
            return self.getToken(at_krl_parser.NUMBER, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_accuracy

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAccuracy" ):
                listener.enterAccuracy(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAccuracy" ):
                listener.exitAccuracy(self)




    def accuracy(self):

        localctx = at_krl_parser.AccuracyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_accuracy)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.match(at_krl_parser.ACCURACY)
            self.state = 486
            self.match(at_krl_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Non_factorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def belief(self):
            return self.getTypedRuleContext(at_krl_parser.BeliefContext,0)


        def accuracy(self):
            return self.getTypedRuleContext(at_krl_parser.AccuracyContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_non_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNon_factor" ):
                listener.enterNon_factor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNon_factor" ):
                listener.exitNon_factor(self)




    def non_factor(self):

        localctx = at_krl_parser.Non_factorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_non_factor)
        try:
            self.state = 493
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 488
                self.belief()
                self.state = 489
                self.accuracy()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 491
                self.belief()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 492
                self.accuracy()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_value(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_valueContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krl_parser.Non_factorContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_value" ):
                listener.enterKb_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_value" ):
                listener.exitKb_value(self)




    def kb_value(self):

        localctx = at_krl_parser.Kb_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_kb_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 495
            self.simple_value()
            self.state = 497
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,50,self._ctx)
            if la_ == 1:
                self.state = 496
                self.non_factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_ref(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_refContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krl_parser.Non_factorContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_reference" ):
                listener.enterKb_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_reference" ):
                listener.exitKb_reference(self)




    def kb_reference(self):

        localctx = at_krl_parser.Kb_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_kb_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.simple_ref()
            self.state = 501
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,51,self._ctx)
            if la_ == 1:
                self.state = 500
                self.non_factor()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_referenceContext,0)


        def kb_value(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_valueContext,0)


        def MINUS(self):
            return self.getToken(at_krl_parser.MINUS, 0)

        def kb_operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Kb_operationContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Kb_operationContext,i)


        def non_factor(self):
            return self.getTypedRuleContext(at_krl_parser.Non_factorContext,0)


        def logical_unary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_unaryContext,0)


        def LPAR(self):
            return self.getToken(at_krl_parser.LPAR, 0)

        def RPAR(self):
            return self.getToken(at_krl_parser.RPAR, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def high_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.High_p_mathContext,0)


        def low_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.Low_p_mathContext,0)


        def compare(self):
            return self.getTypedRuleContext(at_krl_parser.CompareContext,0)


        def logical_binary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_binaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_operation" ):
                listener.enterKb_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_operation" ):
                listener.exitKb_operation(self)



    def kb_operation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = at_krl_parser.Kb_operationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 88
        self.enterRecursionRule(localctx, 88, self.RULE_kb_operation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 526
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [102]:
                self.state = 504
                self.kb_reference()
                pass
            elif token in [103, 104]:
                self.state = 505
                self.kb_value()
                pass
            elif token in [48]:
                self.state = 506
                self.match(at_krl_parser.MINUS)
                self.state = 507
                self.kb_operation(0)
                self.state = 509
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 508
                    self.non_factor()


                pass
            elif token in [67, 73, 86]:
                self.state = 511
                self.logical_unary()
                self.state = 512
                self.kb_operation(0)
                self.state = 514
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 513
                    self.non_factor()


                pass
            elif token in [36]:
                self.state = 516
                self.match(at_krl_parser.LPAR)
                self.state = 518
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 517
                    self.newline()


                self.state = 520
                self.kb_operation(0)
                self.state = 522
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 521
                    self.newline()


                self.state = 524
                self.match(at_krl_parser.RPAR)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 554
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,62,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 552
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
                    if la_ == 1:
                        localctx = at_krl_parser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 528
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 529
                        self.high_p_math()
                        self.state = 530
                        self.kb_operation(0)
                        self.state = 532
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
                        if la_ == 1:
                            self.state = 531
                            self.non_factor()


                        pass

                    elif la_ == 2:
                        localctx = at_krl_parser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 534
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 535
                        self.low_p_math()
                        self.state = 536
                        self.kb_operation(0)
                        self.state = 538
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
                        if la_ == 1:
                            self.state = 537
                            self.non_factor()


                        pass

                    elif la_ == 3:
                        localctx = at_krl_parser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 540
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 541
                        self.compare()
                        self.state = 542
                        self.kb_operation(0)
                        self.state = 544
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
                        if la_ == 1:
                            self.state = 543
                            self.non_factor()


                        pass

                    elif la_ == 4:
                        localctx = at_krl_parser.Kb_operationContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_operation)
                        self.state = 546
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 547
                        self.logical_binary()
                        self.state = 548
                        self.kb_operation(0)
                        self.state = 550
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
                        if la_ == 1:
                            self.state = 549
                            self.non_factor()


                        pass

             
                self.state = 556
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,62,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Kb_evaluatableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allen_evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_evaluatableContext,0)


        def kb_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_referenceContext,0)


        def kb_value(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_valueContext,0)


        def MINUS(self):
            return self.getToken(at_krl_parser.MINUS, 0)

        def kb_evaluatable(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.Kb_evaluatableContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.Kb_evaluatableContext,i)


        def non_factor(self):
            return self.getTypedRuleContext(at_krl_parser.Non_factorContext,0)


        def logical_unary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_unaryContext,0)


        def LPAR(self):
            return self.getToken(at_krl_parser.LPAR, 0)

        def RPAR(self):
            return self.getToken(at_krl_parser.RPAR, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def high_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.High_p_mathContext,0)


        def low_p_math(self):
            return self.getTypedRuleContext(at_krl_parser.Low_p_mathContext,0)


        def compare(self):
            return self.getTypedRuleContext(at_krl_parser.CompareContext,0)


        def logical_binary(self):
            return self.getTypedRuleContext(at_krl_parser.Logical_binaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_evaluatable" ):
                listener.enterKb_evaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_evaluatable" ):
                listener.exitKb_evaluatable(self)



    def kb_evaluatable(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = at_krl_parser.Kb_evaluatableContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 90
        self.enterRecursionRule(localctx, 90, self.RULE_kb_evaluatable, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.state = 558
                self.allen_evaluatable()
                pass

            elif la_ == 2:
                self.state = 559
                self.kb_reference()
                pass

            elif la_ == 3:
                self.state = 560
                self.kb_value()
                pass

            elif la_ == 4:
                self.state = 561
                self.match(at_krl_parser.MINUS)
                self.state = 562
                self.kb_evaluatable(0)
                self.state = 564
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
                if la_ == 1:
                    self.state = 563
                    self.non_factor()


                pass

            elif la_ == 5:
                self.state = 566
                self.logical_unary()
                self.state = 567
                self.kb_evaluatable(0)
                self.state = 569
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
                if la_ == 1:
                    self.state = 568
                    self.non_factor()


                pass

            elif la_ == 6:
                self.state = 571
                self.match(at_krl_parser.LPAR)
                self.state = 573
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 572
                    self.newline()


                self.state = 575
                self.kb_evaluatable(0)
                self.state = 577
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==107:
                    self.state = 576
                    self.newline()


                self.state = 579
                self.match(at_krl_parser.RPAR)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 609
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,73,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 607
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,72,self._ctx)
                    if la_ == 1:
                        localctx = at_krl_parser.Kb_evaluatableContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_evaluatable)
                        self.state = 583
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 584
                        self.high_p_math()
                        self.state = 585
                        self.kb_evaluatable(0)
                        self.state = 587
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,68,self._ctx)
                        if la_ == 1:
                            self.state = 586
                            self.non_factor()


                        pass

                    elif la_ == 2:
                        localctx = at_krl_parser.Kb_evaluatableContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_evaluatable)
                        self.state = 589
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 590
                        self.low_p_math()
                        self.state = 591
                        self.kb_evaluatable(0)
                        self.state = 593
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
                        if la_ == 1:
                            self.state = 592
                            self.non_factor()


                        pass

                    elif la_ == 3:
                        localctx = at_krl_parser.Kb_evaluatableContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_evaluatable)
                        self.state = 595
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 596
                        self.compare()
                        self.state = 597
                        self.kb_evaluatable(0)
                        self.state = 599
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,70,self._ctx)
                        if la_ == 1:
                            self.state = 598
                            self.non_factor()


                        pass

                    elif la_ == 4:
                        localctx = at_krl_parser.Kb_evaluatableContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_kb_evaluatable)
                        self.state = 601
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 602
                        self.logical_binary()
                        self.state = 603
                        self.kb_evaluatable(0)
                        self.state = 605
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,71,self._ctx)
                        if la_ == 1:
                            self.state = 604
                            self.non_factor()


                        pass

             
                self.state = 611
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,73,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Allen_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def simple_ref(self):
            return self.getTypedRuleContext(at_krl_parser.Simple_refContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_allen_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen_reference" ):
                listener.enterAllen_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen_reference" ):
                listener.exitAllen_reference(self)




    def allen_reference(self):

        localctx = at_krl_parser.Allen_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_allen_reference)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 612
            self.simple_ref()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allen_indexed_referenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allen_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_referenceContext,0)


        def index(self):
            return self.getTypedRuleContext(at_krl_parser.IndexContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_allen_indexed_reference

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen_indexed_reference" ):
                listener.enterAllen_indexed_reference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen_indexed_reference" ):
                listener.exitAllen_indexed_reference(self)




    def allen_indexed_reference(self):

        localctx = at_krl_parser.Allen_indexed_referenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_allen_indexed_reference)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 614
            self.allen_reference()
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==37:
                self.state = 615
                self.index()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allen_attribute_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allen_indexed_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_indexed_referenceContext,0)


        def DOT(self):
            return self.getToken(at_krl_parser.DOT, 0)

        def DURATION(self):
            return self.getToken(at_krl_parser.DURATION, 0)

        def OPEN_TACT(self):
            return self.getToken(at_krl_parser.OPEN_TACT, 0)

        def CLOSE_TACT(self):
            return self.getToken(at_krl_parser.CLOSE_TACT, 0)

        def OCCURANCE_TACT(self):
            return self.getToken(at_krl_parser.OCCURANCE_TACT, 0)

        def allen_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_referenceContext,0)


        def OCCURANCE_COUNT(self):
            return self.getToken(at_krl_parser.OCCURANCE_COUNT, 0)

        def OPEN_COUNT(self):
            return self.getToken(at_krl_parser.OPEN_COUNT, 0)

        def CLOSE_COUNT(self):
            return self.getToken(at_krl_parser.CLOSE_COUNT, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_allen_attribute_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen_attribute_expression" ):
                listener.enterAllen_attribute_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen_attribute_expression" ):
                listener.exitAllen_attribute_expression(self)




    def allen_attribute_expression(self):

        localctx = at_krl_parser.Allen_attribute_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_allen_attribute_expression)
        self._la = 0 # Token type
        try:
            self.state = 626
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,75,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 618
                self.allen_indexed_reference()
                self.state = 619
                self.match(at_krl_parser.DOT)
                self.state = 620
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 118489088) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 622
                self.allen_reference()
                self.state = 623
                self.match(at_krl_parser.DOT)
                self.state = 624
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 14680064) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IndexContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSQB(self):
            return self.getToken(at_krl_parser.LSQB, 0)

        def evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.EvaluatableContext,0)


        def RSQB(self):
            return self.getToken(at_krl_parser.RSQB, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_index

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIndex" ):
                listener.enterIndex(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIndex" ):
                listener.exitIndex(self)




    def index(self):

        localctx = at_krl_parser.IndexContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_index)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 628
            self.match(at_krl_parser.LSQB)
            self.state = 629
            self.evaluatable()
            self.state = 630
            self.match(at_krl_parser.RSQB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allen_operationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allen_indexed_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_indexed_referenceContext,0)


        def allen(self):
            return self.getTypedRuleContext(at_krl_parser.AllenContext,0)


        def allen_reference(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_referenceContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_allen_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen_operation" ):
                listener.enterAllen_operation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen_operation" ):
                listener.exitAllen_operation(self)




    def allen_operation(self):

        localctx = at_krl_parser.Allen_operationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_allen_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 632
            self.allen_indexed_reference()
            self.state = 633
            self.allen()
            self.state = 634
            self.allen_reference()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Allen_evaluatableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def allen_operation(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_operationContext,0)


        def allen_attribute_expression(self):
            return self.getTypedRuleContext(at_krl_parser.Allen_attribute_expressionContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_allen_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen_evaluatable" ):
                listener.enterAllen_evaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen_evaluatable" ):
                listener.exitAllen_evaluatable(self)




    def allen_evaluatable(self):

        localctx = at_krl_parser.Allen_evaluatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_allen_evaluatable)
        try:
            self.state = 638
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,76,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 636
                self.allen_operation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 637
                self.allen_attribute_expression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluatableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def kb_evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_evaluatableContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_evaluatable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEvaluatable" ):
                listener.enterEvaluatable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEvaluatable" ):
                listener.exitEvaluatable(self)




    def evaluatable(self):

        localctx = at_krl_parser.EvaluatableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_evaluatable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 640
            self.kb_evaluatable(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_binaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLEVBAR(self):
            return self.getToken(at_krl_parser.DOUBLEVBAR, 0)

        def VBAR(self):
            return self.getToken(at_krl_parser.VBAR, 0)

        def DOUBLEAMPER(self):
            return self.getToken(at_krl_parser.DOUBLEAMPER, 0)

        def AMPER(self):
            return self.getToken(at_krl_parser.AMPER, 0)

        def AND(self):
            return self.getToken(at_krl_parser.AND, 0)

        def OR(self):
            return self.getToken(at_krl_parser.OR, 0)

        def XOR(self):
            return self.getToken(at_krl_parser.XOR, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_logical_binary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_binary" ):
                listener.enterLogical_binary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_binary" ):
                listener.exitLogical_binary(self)




    def logical_binary(self):

        localctx = at_krl_parser.Logical_binaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_logical_binary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 642
            _la = self._input.LA(1)
            if not(((((_la - 51)) & ~0x3f) == 0 and ((1 << (_la - 51)) & 3670031) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_unaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(at_krl_parser.NOT, 0)

        def TILDE(self):
            return self.getToken(at_krl_parser.TILDE, 0)

        def EXCL(self):
            return self.getToken(at_krl_parser.EXCL, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_logical_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_unary" ):
                listener.enterLogical_unary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_unary" ):
                listener.exitLogical_unary(self)




    def logical_unary(self):

        localctx = at_krl_parser.Logical_unaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_logical_unary)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 644
            _la = self._input.LA(1)
            if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 524353) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompareContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQEQUAL(self):
            return self.getToken(at_krl_parser.EQEQUAL, 0)

        def EQUAL(self):
            return self.getToken(at_krl_parser.EQUAL, 0)

        def EQ(self):
            return self.getToken(at_krl_parser.EQ, 0)

        def GREATEREQUAL(self):
            return self.getToken(at_krl_parser.GREATEREQUAL, 0)

        def GREATER(self):
            return self.getToken(at_krl_parser.GREATER, 0)

        def GT(self):
            return self.getToken(at_krl_parser.GT, 0)

        def GE(self):
            return self.getToken(at_krl_parser.GE, 0)

        def LESSEQUAL(self):
            return self.getToken(at_krl_parser.LESSEQUAL, 0)

        def LESS(self):
            return self.getToken(at_krl_parser.LESS, 0)

        def LT(self):
            return self.getToken(at_krl_parser.LT, 0)

        def LE(self):
            return self.getToken(at_krl_parser.LE, 0)

        def NE(self):
            return self.getToken(at_krl_parser.NE, 0)

        def NOTEQUAL(self):
            return self.getToken(at_krl_parser.NOTEQUAL, 0)

        def INEQUAL(self):
            return self.getToken(at_krl_parser.INEQUAL, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_compare

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompare" ):
                listener.enterCompare(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompare" ):
                listener.exitCompare(self)




    def compare(self):

        localctx = at_krl_parser.CompareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_compare)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 646
            _la = self._input.LA(1)
            if not(((((_la - 55)) & ~0x3f) == 0 and ((1 << (_la - 55)) & 2113933195) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class High_p_mathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOUBLESTAR(self):
            return self.getToken(at_krl_parser.DOUBLESTAR, 0)

        def MUL(self):
            return self.getToken(at_krl_parser.MUL, 0)

        def SLASH(self):
            return self.getToken(at_krl_parser.SLASH, 0)

        def DIV(self):
            return self.getToken(at_krl_parser.DIV, 0)

        def PERCENT(self):
            return self.getToken(at_krl_parser.PERCENT, 0)

        def MOD(self):
            return self.getToken(at_krl_parser.MOD, 0)

        def CIRCUMFLEX(self):
            return self.getToken(at_krl_parser.CIRCUMFLEX, 0)

        def STAR(self):
            return self.getToken(at_krl_parser.STAR, 0)

        def POW(self):
            return self.getToken(at_krl_parser.POW, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_high_p_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHigh_p_math" ):
                listener.enterHigh_p_math(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHigh_p_math" ):
                listener.exitHigh_p_math(self)




    def high_p_math(self):

        localctx = at_krl_parser.High_p_mathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_high_p_math)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 648
            _la = self._input.LA(1)
            if not(((((_la - 49)) & ~0x3f) == 0 and ((1 << (_la - 49)) & 1712850947) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Low_p_mathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(at_krl_parser.PLUS, 0)

        def ADD(self):
            return self.getToken(at_krl_parser.ADD, 0)

        def MINUS(self):
            return self.getToken(at_krl_parser.MINUS, 0)

        def SUB(self):
            return self.getToken(at_krl_parser.SUB, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_low_p_math

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLow_p_math" ):
                listener.enterLow_p_math(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLow_p_math" ):
                listener.exitLow_p_math(self)




    def low_p_math(self):

        localctx = at_krl_parser.Low_p_mathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_low_p_math)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 650
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & 6442450953) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AllenContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALLEN_B(self):
            return self.getToken(at_krl_parser.ALLEN_B, 0)

        def ALLEN_BI(self):
            return self.getToken(at_krl_parser.ALLEN_BI, 0)

        def ALLEN_M(self):
            return self.getToken(at_krl_parser.ALLEN_M, 0)

        def ALLEN_MI(self):
            return self.getToken(at_krl_parser.ALLEN_MI, 0)

        def ALLEN_S(self):
            return self.getToken(at_krl_parser.ALLEN_S, 0)

        def ALLEN_SI(self):
            return self.getToken(at_krl_parser.ALLEN_SI, 0)

        def ALLEN_F(self):
            return self.getToken(at_krl_parser.ALLEN_F, 0)

        def ALLEN_FI(self):
            return self.getToken(at_krl_parser.ALLEN_FI, 0)

        def ALLEN_D(self):
            return self.getToken(at_krl_parser.ALLEN_D, 0)

        def ALLEN_DI(self):
            return self.getToken(at_krl_parser.ALLEN_DI, 0)

        def ALLEN_O(self):
            return self.getToken(at_krl_parser.ALLEN_O, 0)

        def ALLEN_OI(self):
            return self.getToken(at_krl_parser.ALLEN_OI, 0)

        def ALLEN_E(self):
            return self.getToken(at_krl_parser.ALLEN_E, 0)

        def ALLEN_A(self):
            return self.getToken(at_krl_parser.ALLEN_A, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_allen

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAllen" ):
                listener.enterAllen(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAllen" ):
                listener.exitAllen(self)




    def allen(self):

        localctx = at_krl_parser.AllenContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_allen)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 652
            _la = self._input.LA(1)
            if not(((((_la - 87)) & ~0x3f) == 0 and ((1 << (_la - 87)) & 16383) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CommentaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def COMMENT(self):
            return self.getToken(at_krl_parser.COMMENT, 0)

        def COMMENT_DATA(self):
            return self.getToken(at_krl_parser.COMMENT_DATA, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_commentary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCommentary" ):
                listener.enterCommentary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCommentary" ):
                listener.exitCommentary(self)




    def commentary(self):

        localctx = at_krl_parser.CommentaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_commentary)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 654
            self.match(at_krl_parser.COMMENT)
            self.state = 655
            self.match(at_krl_parser.COMMENT_DATA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_ruleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RULE(self):
            return self.getToken(at_krl_parser.RULE, 0)

        def NAME(self):
            return self.getToken(at_krl_parser.NAME, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def kb_rule_condition(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_rule_conditionContext,0)


        def kb_rule_instructions(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_rule_instructionsContext,0)


        def TYPE(self):
            return self.getToken(at_krl_parser.TYPE, 0)

        def rule_type(self):
            return self.getTypedRuleContext(at_krl_parser.Rule_typeContext,0)


        def kb_rule_else_instructions(self):
            return self.getTypedRuleContext(at_krl_parser.Kb_rule_else_instructionsContext,0)


        def commentary(self):
            return self.getTypedRuleContext(at_krl_parser.CommentaryContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule" ):
                listener.enterKb_rule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule" ):
                listener.exitKb_rule(self)




    def kb_rule(self):

        localctx = at_krl_parser.Kb_ruleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_kb_rule)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 657
            self.match(at_krl_parser.RULE)
            self.state = 658
            self.match(at_krl_parser.NAME)
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,77,self._ctx)
            if la_ == 1:
                self.state = 659
                self.newline()
                self.state = 660
                self.match(at_krl_parser.TYPE)
                self.state = 661
                self.rule_type()


            self.state = 665
            self.newline()
            self.state = 666
            self.kb_rule_condition()
            self.state = 667
            self.newline()
            self.state = 668
            self.kb_rule_instructions()
            self.state = 672
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,78,self._ctx)
            if la_ == 1:
                self.state = 669
                self.newline()
                self.state = 670
                self.kb_rule_else_instructions()


            self.state = 677
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,79,self._ctx)
            if la_ == 1:
                self.state = 674
                self.newline()
                self.state = 675
                self.commentary()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_simple_type(self):
            return self.getTypedRuleContext(at_krl_parser.Rule_simple_typeContext,0)


        def rule_periodic_type(self):
            return self.getTypedRuleContext(at_krl_parser.Rule_periodic_typeContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_rule_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_type" ):
                listener.enterRule_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_type" ):
                listener.exitRule_type(self)




    def rule_type(self):

        localctx = at_krl_parser.Rule_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_rule_type)
        try:
            self.state = 681
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 679
                self.rule_simple_type()
                pass
            elif token in [29]:
                self.enterOuterAlt(localctx, 2)
                self.state = 680
                self.rule_periodic_type()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_simple_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIMPLE(self):
            return self.getToken(at_krl_parser.SIMPLE, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_rule_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_simple_type" ):
                listener.enterRule_simple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_simple_type" ):
                listener.exitRule_simple_type(self)




    def rule_simple_type(self):

        localctx = at_krl_parser.Rule_simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_rule_simple_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 683
            self.match(at_krl_parser.SIMPLE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_periodic_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_periodic_type_def(self):
            return self.getTypedRuleContext(at_krl_parser.Rule_periodic_type_defContext,0)


        def NUMBER(self):
            return self.getToken(at_krl_parser.NUMBER, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_rule_periodic_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_periodic_type" ):
                listener.enterRule_periodic_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_periodic_type" ):
                listener.exitRule_periodic_type(self)




    def rule_periodic_type(self):

        localctx = at_krl_parser.Rule_periodic_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_rule_periodic_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 685
            self.rule_periodic_type_def()
            self.state = 686
            self.match(at_krl_parser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rule_periodic_type_defContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PERIODIC(self):
            return self.getToken(at_krl_parser.PERIODIC, 0)

        def COLON(self):
            return self.getToken(at_krl_parser.COLON, 0)

        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def PERIOD(self):
            return self.getToken(at_krl_parser.PERIOD, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_rule_periodic_type_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule_periodic_type_def" ):
                listener.enterRule_periodic_type_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule_periodic_type_def" ):
                listener.exitRule_periodic_type_def(self)




    def rule_periodic_type_def(self):

        localctx = at_krl_parser.Rule_periodic_type_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_rule_periodic_type_def)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.match(at_krl_parser.PERIODIC)
            self.state = 693
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [107]:
                self.state = 689
                self.newline()
                self.state = 690
                self.match(at_krl_parser.PERIOD)
                pass
            elif token in [42]:
                self.state = 692
                self.match(at_krl_parser.COLON)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(at_krl_parser.IF, 0)

        def newline(self):
            return self.getTypedRuleContext(at_krl_parser.NewlineContext,0)


        def evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.EvaluatableContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_rule_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_condition" ):
                listener.enterKb_rule_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_condition" ):
                listener.exitKb_rule_condition(self)




    def kb_rule_condition(self):

        localctx = at_krl_parser.Kb_rule_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_kb_rule_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 695
            self.match(at_krl_parser.IF)
            self.state = 696
            self.newline()
            self.state = 697
            self.evaluatable()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_instructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THEN(self):
            return self.getToken(at_krl_parser.THEN, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.InstructionContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.InstructionContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_rule_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_instructions" ):
                listener.enterKb_rule_instructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_instructions" ):
                listener.exitKb_rule_instructions(self)




    def kb_rule_instructions(self):

        localctx = at_krl_parser.Kb_rule_instructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_kb_rule_instructions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self.match(at_krl_parser.THEN)
            self.state = 703 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 700
                    self.newline()
                    self.state = 701
                    self.instruction()

                else:
                    raise NoViableAltException(self)
                self.state = 705 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,82,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Kb_rule_else_instructionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(at_krl_parser.ELSE, 0)

        def newline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.NewlineContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.NewlineContext,i)


        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(at_krl_parser.InstructionContext)
            else:
                return self.getTypedRuleContext(at_krl_parser.InstructionContext,i)


        def getRuleIndex(self):
            return at_krl_parser.RULE_kb_rule_else_instructions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKb_rule_else_instructions" ):
                listener.enterKb_rule_else_instructions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKb_rule_else_instructions" ):
                listener.exitKb_rule_else_instructions(self)




    def kb_rule_else_instructions(self):

        localctx = at_krl_parser.Kb_rule_else_instructionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_kb_rule_else_instructions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 707
            self.match(at_krl_parser.ELSE)
            self.state = 711 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 708
                    self.newline()
                    self.state = 709
                    self.instruction()

                else:
                    raise NoViableAltException(self)
                self.state = 713 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,83,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_instructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ref_path(self):
            return self.getTypedRuleContext(at_krl_parser.Ref_pathContext,0)


        def left_assign(self):
            return self.getTypedRuleContext(at_krl_parser.Left_assignContext,0)


        def evaluatable(self):
            return self.getTypedRuleContext(at_krl_parser.EvaluatableContext,0)


        def non_factor(self):
            return self.getTypedRuleContext(at_krl_parser.Non_factorContext,0)


        def right_assign(self):
            return self.getTypedRuleContext(at_krl_parser.Right_assignContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_assign_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign_instruction" ):
                listener.enterAssign_instruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign_instruction" ):
                listener.exitAssign_instruction(self)




    def assign_instruction(self):

        localctx = at_krl_parser.Assign_instructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_assign_instruction)
        self._la = 0 # Token type
        try:
            self.state = 727
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,86,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 715
                self.ref_path()
                self.state = 716
                self.left_assign()
                self.state = 717
                self.evaluatable()
                self.state = 719
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1 or _la==2:
                    self.state = 718
                    self.non_factor()


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.evaluatable()
                self.state = 722
                self.right_assign()
                self.state = 723
                self.ref_path()
                self.state = 725
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1 or _la==2:
                    self.state = 724
                    self.non_factor()


                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign_instruction(self):
            return self.getTypedRuleContext(at_krl_parser.Assign_instructionContext,0)


        def getRuleIndex(self):
            return at_krl_parser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)




    def instruction(self):

        localctx = at_krl_parser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 138, self.RULE_instruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 729
            self.assign_instruction()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Left_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LEFT_ASSIGN(self):
            return self.getToken(at_krl_parser.LEFT_ASSIGN, 0)

        def EQUAL(self):
            return self.getToken(at_krl_parser.EQUAL, 0)

        def COLON_EQ(self):
            return self.getToken(at_krl_parser.COLON_EQ, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_left_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_assign" ):
                listener.enterLeft_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_assign" ):
                listener.exitLeft_assign(self)




    def left_assign(self):

        localctx = at_krl_parser.Left_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_left_assign)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 731
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 432415932971745280) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Right_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RIGHT_ASSIGN(self):
            return self.getToken(at_krl_parser.RIGHT_ASSIGN, 0)

        def getRuleIndex(self):
            return at_krl_parser.RULE_right_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_assign" ):
                listener.enterRight_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_assign" ):
                listener.exitRight_assign(self)




    def right_assign(self):

        localctx = at_krl_parser.Right_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_right_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 733
            self.match(at_krl_parser.RIGHT_ASSIGN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[37] = self.simple_operation_sempred
        self._predicates[44] = self.kb_operation_sempred
        self._predicates[45] = self.kb_evaluatable_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def simple_operation_sempred(self, localctx:Simple_operationContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         

    def kb_operation_sempred(self, localctx:Kb_operationContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def kb_evaluatable_sempred(self, localctx:Kb_evaluatableContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         




