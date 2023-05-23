from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner, runner
from primer_ejercicio import mensaje
from quinto_ejercicio import alert
from segundo_ejercicio import suma
from tercer_ejercicio import checkBox
from cuarto_ejercicio import checkBoxMult
from quinto_ejercicio import alert


primer_ejercicio = TestLoader().loadTestsFromTestCase(mensaje)
segundo_ejercicio = TestLoader().loadTestsFromTestCase(suma)
tercer_ejercicio = TestLoader().loadTestsFromTestCase(checkBox)
cuarto_ejercicio = TestLoader().loadTestsFromTestCase(checkBoxMult)
quinto_ejercicio = TestLoader().loadTestsFromTestCase(alert)

smoke_test = TestSuite([primer_ejercicio, segundo_ejercicio, tercer_ejercicio, cuarto_ejercicio, quinto_ejercicio])

kwargs = {
    "output": 'smoke-report'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)