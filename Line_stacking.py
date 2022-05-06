import pandas as pd
output = 'result/'

sub_x = pd.read_csv(output + '0.37286XCV.csv')
sub_l = pd.read_csv(output + '0.37333L_CV_S.csv')
sub_ave = pd.DataFrame()
sub_ave['id'] = sub_x.id
sub_ave['trip_duration'] = sub_x.trip_duration*0.6 + sub_l.trip_duration*0.4
sub_ave.to_csv(output + 'ave_submission.csv',index=False)
