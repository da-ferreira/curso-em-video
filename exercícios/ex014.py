print('\n{}Conversor de temperatura em °C para °F.{}'.format('\033[7;35m', '\033[m'))
celsius = float(input('\n{}Informe a temperatura em °C:{} '.format('\033[1;37m', '\033[m')))
fah = (celsius * 9 / 5) + 32

print('\nA temperatura de {}{:.1f}°C{} corresponde a {}{:.1f}°F!{}'.format('\033[1;31m', celsius,
                                                                           '\033[m', '\033[1;31m',
                                                                           fah, '\033[m'))
