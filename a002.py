from speedtest import Speedtest

st = Speedtest()
st.get_servers()
best = st.get_best_server()
ping_result = st.results.ping

print(f"\nEncontrado servidor: {best['host']} localizado em {best['country']}.\n")
print('Sua velocidade de Download é de {:.2f} Mbit/s.'.format(st.download() / 1024 / 1024))
print('Sua velocidade de Upload é de {:.2f} Mbit/s.'.format(st.upload() / 1024 / 1024))
print('Seu PING atual é de {:.2f} ms.\n'.format(ping_result))