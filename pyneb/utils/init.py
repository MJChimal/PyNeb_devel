import numpy as np
import pyneb as pn

ELEM_LIST = ['Ag', 'Al', 'Ar', 'As', 'Au', 'B', 'Ba', 'Be', 'Bi', 'Br',
     'C', 'Ca', 'Cd', 'Ce', 'Cl', 'Co', 'Cr', 'Cs', 'Cu', 'Dy', 'Er', 'Eu', 'F', 'Fe', 'Ga', 'Gd', 'Ge',
     'H', 'He', 'Hf', 'Hg', 'Ho', 'I', 'In', 'Ir', 'K', 'Kr', 'La', 'Li', 'Lu', 'Mg', 'Mn', 'Mo',
     'N', 'Na', 'Nb', 'Nd', 'Ne', 'Ni', 'O', 'Os', 'P', 'Pb', 'Pd', 'Pm', 'Pr', 'Pt',
     'Rb', 'Re', 'Rh', 'Ru', 'S', 'Sb', 'Sc', 'Se', 'Si', 'Sm', 'Sn', 'Sr',
     'Ta', 'Tb', 'Te', 'Tc', 'Th', 'Ti', 'Tl','Tm', 'U', 'V', 'W', 'Xe', 'Y', 'Yb', 'Zn', 'Zr', '3He']
SPEC_LIST = ['1', '2', '3', '4', '5', '6', '7']

def _print_LINE_LABEL_LIST(*args, **kwargs):
    """
    The parameters are passed to getAtomDict. May be the fits directory.
    """
    ##
    # @todo we have to check what are the differences in LINE_LABEL_LIST when changing the fits files
    all_atoms = pn.getAtomDict(*args, **kwargs)
    print("LINE_LABEL_LIST = {}")
    for atom in np.sort(all_atoms.keys()):
        wave = all_atoms[atom].lineList
        opt = (wave < 10000.)
        ir = (wave >= 10000.)
        lines_opt = ["'%.0fA'" % line for line in np.sort(wave[opt])]
        lines_ir = ["'%.1fm'" % line for line in np.sort(wave[ir]) / 1.e4]
        lines = lines_opt + lines_ir
        print("LINE_LABEL_LIST['" + atom + "'] = [" + ', '.join(lines) + "]")

def _check_line_label_list(maxErrorA = 5.e-3, maxErrorm = 5.e-2):
    for ion in LINE_LABEL_LIST:
        if ion not in ('H1', 'He1', 'He2'):
            atom = pn.Atom(atom=ion)
            for line in LINE_LABEL_LIST[ion]:
                #print ion, line
                res = atom.getTransition(line, maxErrorA = maxErrorA, maxErrorm = maxErrorm)
            
LINE_LABEL_LIST = {}
LINE_LABEL_LIST['H1r'] = ['1216A', '1026A', '973A', '6563A', '4861A', '4341A', '4102A', '3970A', '3889A',
                           '3835A', '3798A', '1.87m', '1.28m', '1.09m', '9546A', '9229A', '8750A']
LINE_LABEL_LIST['He1r'] = ['5876A', '2945A', '3188A', '3614A', '3889A', '3965A', '4026A', '4121A', '4388A',
                          '4438A', '4471A', '4713A', '4922A', '5016A', '5048A', '5876A', '6678A', '7065A',
                          '7281A', '9464A', '10830A', '11013A', '11969A', '12527A', '12756A', '12785A',
                          '12790A', '12846A', '12968A', '12985A', '13412A', '15084A', '17003A', '18556A',
                          '18685A', '18697A', '19089A', '19543A', '20425A', '20581A', '20602A', '21120A',
                          '21132A', '21608A', '21617A']
LINE_LABEL_LIST['He2r'] = ['1640A', '1215A', '1084A', '4686A', '3203A','6560A', '5411A','4859A', '4541A', '6407A', 
                           '4198A']
LINE_LABEL_LIST['3He2'] = ['3.50c']
LINE_LABEL_LIST['Al2'] = ['2674A', '2670A', '2661A', '1671A', '4451A', '4463A', '4488A', '164.2m', '54.1m', '80.7m']
LINE_LABEL_LIST['Ar2'] = ['7.0m']
LINE_LABEL_LIST['Ar3'] = ['7136A', '7751A', '8036A', '3005A', '3109A', '3154A', '5192A', '9.0m', '6.37m', '21.8m']
LINE_LABEL_LIST['Ar4'] = ['4740A', '4711A', '2868A', '7263A', '7332A', '2854A', '7170A', '7237A', '77.4m', '56.2m']
LINE_LABEL_LIST['Ar5'] = ['6133A', '6435A', '7005A', '2637A', '2692A', '2786A', '4626A', '1218A', '1229A', '1249A', 
                          '1520A', '2262A', '13.1m', '4.93m', '7.9m']
LINE_LABEL_LIST['Ba2'] = ['4935A', '6497A', '6854A', '4555A', '5854A', '6142A', '2361A', '2668A', '2726A', '4524A', 
                          '4900A', '2.05m', '1.76m', '12.5m', '5.9m']
LINE_LABEL_LIST['Ba4'] = ['5697A']
LINE_LABEL_LIST['Br3'] = ['6646A', '6133A', '3714A', '8420A', '9419A', '3498A', '7385A', '8142A', '7.94m', '6.0m']
LINE_LABEL_LIST['C1'] = ['9808A', '9824A', '9850A', '4618A', '4621A', '4627A', '8728A', '2963A', '2965A', '2967A', 
                         '4246A', '8271A', '609.6m', '230.3m', '370.3m']
LINE_LABEL_LIST['C2'] = ['2325A', '2328A', '2323A', '2327A', '2322A', '2325A', '1335A', '1336A', '3131A', '3133A', 
                         '3136A', '1036A', '1037A', '1869A', '1870A', '1871A', '4636A', '4637A', '157.6m', '454.4m', 
                         '198.8m', '353.3m', '3967.2m']
LINE_LABEL_LIST['C2r'] =  ['9903+', '4267+', '7231+', '6580+', '2837+', '1761+', '1335+']
LINE_LABEL_LIST['C3'] = ['1910A', '1909A', '1907A', '977A', '2000A', '2001A', '2003A', '422.0m', '124.9m', '177.4m']
LINE_LABEL_LIST['C4'] = ['1551A', '1548A', '92.8m']
LINE_LABEL_LIST['Ca2'] = ['7292A', '7324A']
LINE_LABEL_LIST['Ca5'] = ['5309A', '6087A', '6428A', '2280A', '2413A', '2464A', '3998A', '4.16m', '3.05m', '11.5m']
LINE_LABEL_LIST['Cl2'] = ['8579A', '9124A', '9381A', '3586A', '3678A', '3719A', '6162A', '14.4m', '10.0m', '33.3m']
LINE_LABEL_LIST['Cl3'] = ['5538A', '5518A', '3353A', '8500A', '8548A', '3343A', '8434A', '8481A', '151.5m', '108.0m']
LINE_LABEL_LIST['Cl4'] = ['7261A', '7531A', '8046A', '3071A', '3119A', '3204A', '5323A',  '1463A', '1474A', '1493A', 
                          '1833A', '2793A', '20.3m', '7.45m', '11.8m']
LINE_LABEL_LIST['Fe3'] = ['4009A', '4659A', '4668A', '4701A', '4734A', '4755A', '5011A', '5085A', '5270A', '4881A', 
                          '4925A', '4931A', '5412A', '4987A', '8729A', '8838A', '3240A', '3286A', '3319A', 
                          '3323A', '3335A', '3355A', '3357A', '3366A', '3371A', '3406A', '4046A', '4080A', '4097A', 
                          '4607A', '4770A', '4778A', '9701A', '9960A', '5440A', '6096A']
LINE_LABEL_LIST['Fe4'] = ['4491A', '5685A', '5735A', '6740A']
LINE_LABEL_LIST['Fe5'] = ['3783A', '3795A', '3822A', '3891A', '3895A', '3911A', '4071A', '4181A', '4227A']
LINE_LABEL_LIST['Fe6'] = ['3556A', '3929A', '5146A', '5176A', '5278A', '5335A', '5370A', '5424A', '5427A', '5485A', '5631A', '5677A']
LINE_LABEL_LIST['Fe7'] = ['5159A', '5276A', '5721A', '6087A']
LINE_LABEL_LIST['K4'] = ['6102A', '6796A', '7109A', '2594A', '2711A', '2760A', '4511A', '6.0m', '4.3m', '15.4m']
LINE_LABEL_LIST['K5'] = ['4163A', '4123A', '2514A', '6349A', '6446A', '2495A', '6222A', '6316A', '42.2m', '31.0m']
LINE_LABEL_LIST['K6'] = ['5602A', '6229A']
LINE_LABEL_LIST['Kr3'] = ['6827A', '9902A', '3022A', '3504A', '3600A', '5423A', '2.2m', '1.88m', '13.1m', '1.07m']
LINE_LABEL_LIST['Kr4'] = ['5868A', '5346A', '3219A', '7131A', '8091A', '2993A', '6108A', '6798A', '6.0m', '4.26m']
LINE_LABEL_LIST['Kr5'] = ['5069A', '6256A', '8243A', '2550A', '2819A', '3163A', '5132A', '2.67m', '1.32m', '2.6m']
LINE_LABEL_LIST['Mg4'] = ['4.5m']
LINE_LABEL_LIST['Mg5'] = ['2783A', '2929A', '2992A', '1294A', '1325A', '1338A', '2418A', '5.6m', '3.96m', '13.5m']
LINE_LABEL_LIST['Mg7'] = ['2441A', '2509A', '2629A', '1174A', '1190A', '1216A', '2261A', '943A', '953A', '970A', 
                          '1537A', '4790A', '9.0m', '3.42m', '5.5m']
LINE_LABEL_LIST['N1'] = ['5200A', '5198A', '3467A', '3466A']
LINE_LABEL_LIST['N2'] = ['6527A', '6548A', '6584A', '3058A', '3063A', '3071A', '5755A', '2137A', '2139A', '2143A', 
                         '3177A', '7092A', '205.3m', '76.4m', '121.8m']
LINE_LABEL_LIST['N2r'] = ['4026.08A', '4035.08A', '4039.35A', '4041.31A', '4043.53A', '4044.78A',
                          '4056.90A', '4058.16A', '4073.04A', '4076.91A', '4077.40A', '4082.27A',
                          '4082.89A', '4086.83A', '4087.30A', '4095.90A', '4096.58A', '4100.97A',
                          '4601.48A', '4607.16A', '4613.87A', '4621.39A', '4630.54A', '4643.09A',
                          '4774.24A', '4779.72A', '4781.19A', '4788.13A', '4793.65A', '4803.29A',
                          '4810.31A', '5001.14A', '5001.48A', '5005.15A', '5016.39A', '5025.66A',
                          '5040.72A', '5452.08A', '5454.22A', '5462.59A', '5478.10A', '5480.06A',
                          '5495.67A', '5666.63A', '5676.02A', '5679.56A', '5686.21A', '5710.77A',
                          '5730.65A', '5927.81A', '5931.78A', '5940.24A', '5941.65A', '5952.39A',
                          '5960.90A']
LINE_LABEL_LIST['N3'] = ['1749A', '1754A', '1747A', '1752A', '1744A', '1750A', '990A', '992A', '2280A', '2284A', 
                         '2288A', '2280A', '2283A', '2287A', '763A', '764A', '1356A', '1357A', '3334A', 
                         '3335A', '57.4m', '167.5m', '71.0m', '123.3m', '1492.1m']
LINE_LABEL_LIST['N4'] = ['1488A', '1487A', '1483A', '765A', '1575A', '1576A', '1580A', '158.4m', '48.3m', '69.4m']
LINE_LABEL_LIST['N5'] = ['1239A', '1243A']
LINE_LABEL_LIST['Na3'] = ['7.3m']
LINE_LABEL_LIST['Na4'] = ['3242A', '3362A', '3416A', '1504A', '1529A', '1540A', '2804A', '9.0m', '6.34m', '21.3m']
LINE_LABEL_LIST['Na6'] = ['2816A', '2872A', '2972A', '1343A', '1356A', '1378A', '2569A', '14.39m', '5.4m', '8.6m']
LINE_LABEL_LIST['Ne2'] = ['12.8m']
LINE_LABEL_LIST['Ne3'] = ['3869A', '3968A', '4012A', '1794A', '1815A', '1824A', '3343A', '15.6m', '10.9m', '36.0m']
LINE_LABEL_LIST['Ne4'] = ['2425A', '2422A', '1602A', '4716A', '4726A', '1601A', '4714A', '4724A', '224.9m', '1579.3m']
LINE_LABEL_LIST['Ne5'] = ['3300A', '3346A', '3426A', '1565A', '1575A', '1592A', '2973A', '1132A', '1137A', '1146A', 
                          '1721A', '4083A', '24.3m', '9.0m', '14.3m']
LINE_LABEL_LIST['Ne6'] = ['997A', '1010A', '993A', '1006A', '986A', '999A', '559A', '563A', '1271A', '1278A', '1289A', 
                          '559A', '563A', '1270A', '1277A', '1288A', '433A', '436A', '766A', '769A', '772A', '1928A', 
                          '1929A', '7.65m', '22.7m', '9.2m', '15.5m', '334.4m']
LINE_LABEL_LIST['Ni3'] = ['7890A', '8500A', '6000A', '6401A', '6534A', '6682A', '6797A', '7125A', '6946A']
LINE_LABEL_LIST['O1'] = ['6300A', '6364A', '6392A', '2959A', '2973A', '2979A', '5577A', '63.2m', '44.1m', '145.5m']
LINE_LABEL_LIST['O1r'] = ['8447+', '7773+', '9264+', '3947+', '1357+']
LINE_LABEL_LIST['O2'] = ['3729A', '3726A', '2470A', '7319A','7320A', '7330A', '7331A', '2470A', '834A', '1075A', 
                         '1260A', '833A', '1073A', '1258A', '833A', '1072A', '1256A', '499.3m', '5023.7m', '61.3m', 
                         '40.7m', '121.3m']
LINE_LABEL_LIST['O2r'] = ['4638.86A', '4641.81A', '4649.13A', '4650.84A', '4661.63A', '4673.73A', '4676.23A', 
                          '4696.35A', '4317.14A', '4336.86A', '4345.56A', '4349.43A', '4366.89A', '4414.90A', 
                          '4416.97A', '4069.62A', '4069.88A', '4072.15A', '4075.86A', '4078.84A', '4085.11A', 
                          '4092.93A', '4590.97A', '4596.18A', '4121.46A', '4132.80A', '4153.30A', '4104.99A', 
                          '4110.79A', '4119.22A', '4120.28A', '4185.44A', '4189.79A', '4087.15A', '4089.29A', 
                          '4095.64A', '4097.26A', '4275.55A', '4282.96A']
LINE_LABEL_LIST['O3'] = ['4931A', '4959A', '5007A', '2315A', '2321A', '2331A', '4363A', '1658A', '1661A', '1666A', 
                         '2497A', '5833A', '88.3m', '32.6m', '51.8m']
LINE_LABEL_LIST['O4'] = ['1400A', '1407A', '1397A', '1405A', '1394A', '1401A', '788A', '1801A', '1806A', '1812A', 
                         '608A', '610A', '1076A', '1078A', '1080A', '2671A', '2672A', '25.9m', '76.7m', '31.7m', 
                         '53.9m', '719.2m']
LINE_LABEL_LIST['O5'] = ['1220A', '1218A', '1214A', '630A', '1301A', '1303A', '1309A', '73.5m', '22.6m', '32.6m']
LINE_LABEL_LIST['Rb4'] = ['5760A', '9009A', '9604A', '2603A', '3110A', '3178A', '4750A', '1.6m', '1.44m', '14.5m']
LINE_LABEL_LIST['Rb5'] = ['5364A', '4742A', '2873A', '6188A', '7290A', '2609A', '5080A', '5800A', '4.1m', '2.84m']
LINE_LABEL_LIST['Rb6'] = ['4210A', '5373A', '7220A', '2212A', '2495A', '2832A', '4660A', '1.95m', '1.01m', '2.1m']
LINE_LABEL_LIST['S2'] = ['6731A', '6716A', '4076A', '4069A', '1260A', '1549A', '1550A', '1823A', '1824A', '1254A', 
                         '1541A', '1542A', '1811A', '1812A', '1251A', '1536A', '1537A', '1804A', '1806A', '314.5m', 
                         '1.03m', '214.0m', '27.7m', '17.6m', '48.6m']
LINE_LABEL_LIST['S3'] = ['8829A', '9069A', '9531A', '3681A', '3722A', '3798A', '6312A', '33.5m', '12.0m', '18.7m']
LINE_LABEL_LIST['S4'] = ['1405A', '1424A', '1398A', '1417A', '1387A', '1406A', '10.5m', '29.0m', '11.2m', '18.3m']
LINE_LABEL_LIST['Se3'] = ['7671A', '8854A', '3516A', '3746A', '4082A', '6493A', '5.74m', '2.54m', '4.55m', '1.1m']
LINE_LABEL_LIST['Se4'] = ['2.28m']
LINE_LABEL_LIST['Si2'] = ['2335A', '2351A', '2329A', '2345A', '2320A', '1808A', '1817A', '8007A', '8077A', '8193A', 
                          '7997A', '8067A', '8183A', '34.8m', '92.3m', '35.2m', '57.1m', '631.5m']
LINE_LABEL_LIST['Si3'] = ['1897A', '1892A', '1883A', '1206A', '3315A', '3329A', '3359A', '77.7m', '25.7m', '38.2m']
LINE_LABEL_LIST['Si4'] = ['1394A', '1403A']
LINE_LABEL_LIST['Xe3'] = ['5847A', '2769A', '3574A', '3800A', '5261A', '1.23m', '1.02m', '6.0m', '1.11m', '1.37m']
LINE_LABEL_LIST['Xe4'] = ['7535A', '5709A', '3566A', '6769A', '9498A', '2804A', '4467A', '5511A', '2.36m', '1.31m']
LINE_LABEL_LIST['Xe6'] = ['6409A']





OLD_LINE_LABEL_LIST = {}
OLD_LINE_LABEL_LIST['H1'] = ['3750A', '3771A', '3889A', '4102A', '4340A', '4861A', '6563A', '9015A', '9229A']
OLD_LINE_LABEL_LIST['He1'] = ['5876A', '2945A', '3188A', '3614A', '3889A', '3965A', '4026A', '4121A', '4388A',
                          '4438A', '4472A', '4713A', '4922A', '5016A', '5048A', '5876A', '6678A', '7065A',
                          '7281A', '9464A', '10830A', '11013A', '11969A', '12527A', '12756A', '12785A',
                          '12790A', '12846A', '12968A', '12985A', '13412A', '15084A', '17003A', '18556A',
                          '18685A', '18697A', '19089A', '19543A', '20425A', '20581A', '20602A', '21120A',
                          '21132A', '21608A', '21617A']
OLD_LINE_LABEL_LIST['He2'] = ['4686A', '5876A']
OLD_LINE_LABEL_LIST['Al2'] = ['2674A', '2670A', '2661A', '1671A', '4453A', '4465A', '4490A', '162.3m', '53.9m', '80.7m']
OLD_LINE_LABEL_LIST['Ar2'] = ['7.0m']
OLD_LINE_LABEL_LIST['Ar3'] = ['7136A', '7751A', '8036A', '3005A', '3109A', '3157A', '5192A', '9.0m', '6.4m', '21.8m']
OLD_LINE_LABEL_LIST['Ar4'] = ['4740A', '4711A', '2868A', '7263A', '7331A', '2854A', '7170A', '7237A', '77.4m', '56.4m']
OLD_LINE_LABEL_LIST['Ar5'] = ['6133A', '6435A', '7005A', '2637A', '2692A', '2786A', '4626A', '13.1m', '4.9m', '7.9m']
OLD_LINE_LABEL_LIST['Ba2'] = ['4935A', '6499A', '6856A', '4555A', '5855A', '6143A', '2361A', '2668A', '2726A', '4526A', '4901A', '2.1m', '1.8m', '12.5m', '5.9m']
OLD_LINE_LABEL_LIST['Ba4'] = ['5698A']
OLD_LINE_LABEL_LIST['Br3'] = ['6646A', '6133A', '3714A', '8420A', '9419A', '3498A', '7385A', '8142A', '7.9m', '6.0m']
OLD_LINE_LABEL_LIST['C1'] = ['9807A', '9823A', '9849A', '4618A', '4621A', '4627A', '8728A', '609.7m', '230.0m', '369.3m']
OLD_LINE_LABEL_LIST['C2'] = ['2325A', '2328A', '2324A', '2327A', '2323A', '2326A', '1335A', '1336A', '3132A', '3134A', '3136A', '1324A', '1326A', '3078A', '3080A', '3081A', '1036A', '1037A', '1870A', '1871A', '4638A', '4763A', '157.8m', '540.2m', '270.1m', '540.0m', '17.6m']
OLD_LINE_LABEL_LIST['C3'] = ['1910A', '1909A', '1907A', '977A', '2001A', '2002A', '2004A', '416.7m', '125.0m', '178.6m']
OLD_LINE_LABEL_LIST['C4'] = ['1548A', '1551A']
OLD_LINE_LABEL_LIST['Ca5'] = ['5311A', '6087A', '6428A', '2280A', '2414A', '2464A', '3999A', '4.2m', '3.0m', '11.5m']
OLD_LINE_LABEL_LIST['Cl2'] = ['8579A', '9124A', '9356A', '3588A', '3678A', '3717A', '6165A', '14.4m', '10.4m', '37.2m']
OLD_LINE_LABEL_LIST['Cl3'] = ['5538A', '5518A', '3353A', '8500A', '8548A', '3343A', '8434A', '8481A', '153.2m', '107.5m']
OLD_LINE_LABEL_LIST['Cl4'] = ['7261A', '7531A', '8046A', '3071A', '3119A', '3204A', '5323A', '20.4m', '7.5m', '11.8m']
OLD_LINE_LABEL_LIST['Fe3'] = ['4009A', '4659A', '4668A', '4703A', '4735A', '4756A', '5013A', '5086A', '5272A', '4882A', '4926A', '4932A', '5413A', '4987A', '4989A', '8731A', '8840A']
OLD_LINE_LABEL_LIST['K4'] = ['6102A', '6796A', '7110A', '2594A', '2711A', '2760A', '4511A', '6.0m', '4.3m', '15.4m']
OLD_LINE_LABEL_LIST['K5'] = ['4163A', '4123A', '2514A', '6349A', '6446A', '2495A', '6223A', '6316A', '42.2m', '31.4m']
OLD_LINE_LABEL_LIST['Kr3'] = ['6827A', '9902A', '3022A', '3504A', '3600A', '5423A', '2.2m', '1.9m', '13.1m', '1.1m']
OLD_LINE_LABEL_LIST['Kr4'] = ['5868A', '5346A', '3219A', '7131A', '8091A', '2993A', '6108A', '6798A', '6.0m', '4.3m']
OLD_LINE_LABEL_LIST['Kr5'] = ['5069A', '6256A', '8243A', '2550A', '2819A', '3163A', '5132A', '2.7m', '1.3m', '2.6m']
OLD_LINE_LABEL_LIST['Mg5'] = ['2783A', '2929A', '2994A', '1294A', '1325A', '1338A', '2418A', '5.6m', '4.0m', '13.5m']
OLD_LINE_LABEL_LIST['Mg7'] = ['2441A', '2509A', '2629A', '1174A', '1190A', '1216A', '2261A', '847A', '855A', '868A', '1296A', '3034A', '9.0m', '3.4m', '5.5m']
OLD_LINE_LABEL_LIST['N1'] = ['5200A', '5198A', '3467A', '3466A', '1094.1m', '1.0m', '27777.8m']
OLD_LINE_LABEL_LIST['N2'] = ['6527A', '6548A', '6584A', '3058A', '3063A', '3071A', '5755A', '2142A', '2144A', '2148A', '3188A', '7147A', '205.4m', '76.3m', '121.5m']
OLD_LINE_LABEL_LIST['N3'] = ['1749A', '1754A', '1747A', '1752A', '1744A', '1750A', '990A', '992A', '2284A', '2287A', '2291A', '990A', '992A', '2283A', '2287A', '2291A', '764A', '765A', '1356A', '1357A', '1359A', '3338A', '3340A', '57.4m', '167.5m', '71.2m', '123.8m', '909.1m']
OLD_LINE_LABEL_LIST['N4'] = ['1488A', '1487A', '1483A', '765A', '1574A', '1576A', '1580A', '158.7m', '48.3m', '69.4m']
OLD_LINE_LABEL_LIST['Na4'] = ['3242A', '3362A', '3416A', '1504A', '1529A', '1540A', '2805A', '9.0m', '6.3m', '21.3m']
OLD_LINE_LABEL_LIST['Na6'] = ['2815A', '2871A', '2970A', '1343A', '1356A', '1377A', '2569A', '14.3m', '5.4m', '8.6m']
OLD_LINE_LABEL_LIST['Ne2'] = ['12.8m']
OLD_LINE_LABEL_LIST['Ne3'] = ['3869A', '3968A', '4012A', '1794A', '1815A', '1824A', '3343A', '15.6m', '10.9m', '36.0m']
OLD_LINE_LABEL_LIST['Ne4'] = ['2425A', '2422A', '1602A', '4716A', '4726A', '1601A', '4714A', '4724A', '221.2m', '1587.3m']
OLD_LINE_LABEL_LIST['Ne5'] = ['3300A', '3346A', '3426A', '1565A', '1575A', '1592A', '2975A', '1132A', '1137A', '1146A', '1722A', '4090A', '24.2m', '9.0m', '14.3m']
OLD_LINE_LABEL_LIST['Ne6'] = ['1005A', '1017A', '999A', '1011A', '993A', '1006A', '567A', '572A', '1309A', '1316A', '1324A', '567A', '572A', '1305A', '1313A', '1324A', '7.6m', '22.4m', '9.2m', '15.6m', '909.1m']
OLD_LINE_LABEL_LIST['O1'] = ['6300A', '6364A', '6392A', '2959A', '2973A', '2979A', '5579A', '63.2m', '44.1m', '145.5m']
OLD_LINE_LABEL_LIST['O2'] = ['3729A', '3726A', '2470A', '7319A', '7330A', '2470A', '7318A', '7329A', '834A', '1075A', '1260A', '833A', '1073A', '1258A', '833A', '1072A', '1256A', '505.3m', '5076.1m', '61.3m', '40.8m', '121.8m']
OLD_LINE_LABEL_LIST['O3'] = ['4931A', '4959A', '5007A', '2315A', '2321A', '2331A', '4363A', '1658A', '1661A', '1666A', '2497A', '5839A', '87.6m', '32.5m', '51.8m']
OLD_LINE_LABEL_LIST['O4'] = ['1400A', '1407A', '1397A', '1405A', '1394A', '1401A', '788A', '791A', '1804A', '1808A', '1814A', '788A', '790A', '1803A', '1808A', '1814A', '609A', '610A', '1077A', '1079A', '1081A', '2673A', '2674A', '25.9m', '76.0m', '31.7m', '54.3m', '588.2m']
OLD_LINE_LABEL_LIST['O5'] = ['1220A', '1218A', '1214A', '630A', '1301A', '1303A', '1309A', '71.6m', '22.6m', '33.0m']
OLD_LINE_LABEL_LIST['Rb4'] = ['5760A', '9009A', '9604A', '2603A', '3110A', '3178A', '4750A', '1.6m', '1.4m', '14.5m']
OLD_LINE_LABEL_LIST['Rb5'] = ['5364A', '4742A', '2873A', '6188A', '7290A', '2609A', '5080A', '5800A', '4.1m', '2.8m']
OLD_LINE_LABEL_LIST['Rb6'] = ['4210A', '5373A', '7220A', '2212A', '2495A', '2832A', '4660A', '1.9m', '1.0m', '2.1m']
OLD_LINE_LABEL_LIST['S2'] = ['6731A', '6716A', '4076A', '4069A', '1260A', '1549A', '1550A', '1823A', '1824A', '1254A', '1541A', '1542A', '1811A', '1812A', '1251A', '1536A', '1537A', '1804A', '1806A', '314.5m', '1.0m', '214.0m', '27.7m', '17.6m', '48.6m']
OLD_LINE_LABEL_LIST['S3'] = ['8829A', '9069A', '9531A', '3681A', '3722A', '3798A', '6312A', '33.6m', '12.0m', '18.7m']
OLD_LINE_LABEL_LIST['S4'] = ['1405A', '1424A', '1398A', '1417A', '1387A', '1406A', '10.5m', '29.2m', '11.2m', '18.3m']
OLD_LINE_LABEL_LIST['Se3'] = ['7671A', '8854A', '3516A', '3746A', '4082A', '6493A', '5.7m', '2.5m', '4.6m', '1.1m']
OLD_LINE_LABEL_LIST['Se4'] = ['2.3m']
OLD_LINE_LABEL_LIST['Si2'] = ['2335A', '2351A', '2329A', '2345A', '2320A', '2335A', '1808A', '1817A', '8009A', '8080A', '8196A', '1808A', '1817A', '7999A', '8070A', '8185A', '34.8m', '91.7m', '35.2m', '57.1m', '646.8m']
OLD_LINE_LABEL_LIST['Si3'] = ['1897A', '1892A', '1883A', '1206A', '3316A', '3330A', '3359A', '78.0m', '25.7m', '38.3m']
OLD_LINE_LABEL_LIST['Xe3'] = ['5847A', '2769A', '3574A', '3800A', '5261A', '1.2m', '1.0m', '6.0m', '1.1m', '1.4m']
OLD_LINE_LABEL_LIST['Xe4'] = ['7535A', '5709A', '3566A', '6769A', '9498A', '2804A', '4467A', '5511A', '2.4m', '1.3m']
OLD_LINE_LABEL_LIST['Xe6'] = ['6409A']

BLEND_LIST = {}
BLEND_LIST['C2_2325A+'] = 'I(3,1)+I(3,2)+I(4,1)+I(4,2)+I(5,1)+I(5,2)'
BLEND_LIST['C2_1335A+'] = 'I(6,1)+I(6,2)+I(7,1)+I(7,2)'
BLEND_LIST['C3_1909A+'] = 'I(4,1)+I(3,1)+I(2,1)'
BLEND_LIST['C3_2000A+'] = 'I(5,4)+I(5,3)+I(5,2)'
BLEND_LIST['C4_1550A+'] = 'I(2,1)+I(3,1)'
BLEND_LIST['N1_5199A+'] = 'I(2,1)+I(3,1)'
BLEND_LIST['N1_3466A+'] = 'I(4,1)+I(5,1)'
BLEND_LIST['N1_1.0m+'] = 'I(4,2)+I(4,3)+I(5,2)+I(5,3)'
BLEND_LIST['N3_1750A+'] = 'I(3,1)+I(3,2)+I(4,1)+I(4,2)+I(5,1)+I(5,2)'
BLEND_LIST['N4_1485A+'] = 'I(4,1)+I(3,1)'
BLEND_LIST['N5_1240A+'] = 'I(2,1)+I(3,1)'
BLEND_LIST['O2_3727A+'] = 'L(3726)+L(3729)'
BLEND_LIST['O2_1075A+'] = 'I(6,2)+I(6,3)'
BLEND_LIST['O2_3727A+'] = 'I(2,1)+I(3,1)'
BLEND_LIST['O2_7330A+'] = 'I(4,3)+I(5,3)'
BLEND_LIST['O2_7319A+'] = 'I(4,2)+I(5,2)'
BLEND_LIST['O2_7325A+'] = 'I(4,2)+I(5,2)+I(4,3)+I(5,3)'
BLEND_LIST['O3_1664A+'] = 'L(1660)+L(1666)'
BLEND_LIST['O4_1401A+'] = 'I(3,1)+I(3,2)+I(4,1)+I(4,2)+I(5,1)+I(5,2)'
BLEND_LIST['O4_1400A+'] = 'I(3,1)+I(4,1)+I(5,2)'
BLEND_LIST['N3_1751A+'] = 'I(3,1)+I(3,2)+I(4,1)+I(4,2)+I(5,1)+I(5,2)'
BLEND_LIST['Ne4_4726A+'] = 'L(4725)+L(4727)'
BLEND_LIST['Ne4_2423A+'] = 'I(2,1)+I(3,1)'
BLEND_LIST['S2_6725A+'] = 'L(6716)+L(6731)'
BLEND_LIST['S2_4072A+'] = 'L(4076)+L(4069)'

label2levelDict = {'Fe3_4668A': (14, 2), 
                   'Fe3_5013A': (10, 3),
                   'Fe3_3355A': (21, 4)}


