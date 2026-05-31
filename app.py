import streamlit as st
import pickle
import pandas as pd

# 1. നമ്മൾ നേരത്തെ സേവ് ചെയ്ത മോഡൽ ലോഡ് ചെയ്യുന്നു
model = pickle.load(open('model.pkl', 'rb'))

# 2. വെബ്സൈറ്റിന്റെ തലക്കെട്ട് (Title)
st.title('🎓 Student Placement Predictor')
st.write('നിങ്ങളുടെ പഠന വിവരങ്ങൾ നൽകൂ, ജോലി കിട്ടുമോ എന്ന് നോക്കാം!')

# 3. ഉപയോക്താവിന് വിവരങ്ങൾ നൽകാനുള്ള ബോക്സുകൾ
study_hours = st.number_input('ദിവസം എത്ര മണിക്കൂർ പഠിക്കും?', min_value=0, max_value=24, value=5)
attendance = st.slider('സ്കൂളിലെ അറ്റൻഡൻസ് (%)', 0, 100, 80)
previous_score = st.number_input('കഴിഞ്ഞ പരീക്ഷയിലെ മാർക്ക് (0-100)', 0, 100, 75)

# 4. പ്രവചനം നടത്താനുള്ള ബട്ടൺ
if st.button('Predict My Future'):
    # ഇൻപുട്ടുകൾ ഒരു ഡാറ്റാഫ്രെയിം ആക്കുന്നു
    input_data = pd.DataFrame([[study_hours, attendance, previous_score]], 
                              columns=['study_hours', 'attendance', 'previous_score'])
    
    # മോഡൽ ഉപയോഗിച്ച് പ്രവചിക്കുന്നു
    prediction = model.predict(input_data)
    
    # റിസൾട്ട് കാണിക്കുന്നു
    if prediction[0] == 1:
        st.success('🎉 Congratulations! You are likely to be PLACED.')
    else:
        st.error('⚠️ Work Hard! You might NOT get placed this time.')
