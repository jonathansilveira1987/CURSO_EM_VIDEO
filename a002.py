from speedtest import Speedtest

st = Speedtest()

print('Sua conexão de download é: ', st.download())
print('Sua conexão de upload é: ', st.upload())