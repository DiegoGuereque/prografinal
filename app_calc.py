import streamlit as st
st.title('Calculadora de calorías quemadas')
st.write('Utiliza nuestra **calculadora de calorías quemadas** para lograr adelgazar o aumentar de peso.')
st.image('verduras.gif')

minutos = st.number_input('Ingresa cuántos minutos de ejercicio realizaste',0,10000)

ejercicio = st.selectbox('Selecciona el ejercicio que realizaste',('Levantamiento de pesas','Aerobics','Yoga','Boxeo','Ciclismo','Calistenia','Circuito','Billar','Fútbol','Voleibol','Basketball','Natación','Bailar','Caminar (6.5 km/h)','Correr','Dormir','Ver TV','Leer un libro','Cocinar','Cuidar niños','Estar sentado en clase'))

if ejercicio == 'Levantamiento de pesas':
  calorias=112
if ejercicio=='Fútbol':
  calorias=260
if ejercicio =='Aerobics':
  calorias=205
if ejercicio=='Yoga':
  calorias=149
if ejercicio=='Boxeo':
  calorias=335
if ejercicio=='Ciclismo':
  calorias=391
if ejercicio=='Calistenia':
  calorias=298
if ejercicio=='Billar':
  calorias==93
if ejercicio=='Voleibol':
  calorias=112
if ejercicio=='Basketball':
  calorias=298
if ejercicio=='Natacion':
  calorias=223
if ejercicio=='Bailar':
  calorias=205
if ejercicio=='Caminar (6.5 km/h)':
  calorias=167
if ejercicio=='Correr':
  calorias=335
if ejercicio=='Circuito':
  calorias=298
if ejercicio=='Dormir':
  calorias=28
if ejercicio=='Ver TV':
  calorias=33
if ejercicio=='Leer un libro':
  calorias=50
if ejercicio=='Cocinar':
  calorias=93
if ejercicio=='Cuidar niños':
  calorias==130
if ejercicio=='Estar sentado en clase':
  calorias=65
result=(calorias*minutos)/30

if st.button('Calcular'):
  st.success('¡Felicidades!, quemaste **'+str(result)+' calorías**')
  st.balloons()
  
st.markdown('[Fuentes](https://www.health.harvard.edu/diet-and-weight-loss/calories-burned-in-30-minutes-for-people-of-three-different-weights)')

