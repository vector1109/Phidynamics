import os
import importlib.util
import sys

def verificar():
    scripts = [f for f in os.listdir('.') if f.endswith('.py') and f != 'verificar_todo.py']
    
    print(f"{'ARCHIVO':<30} | {'ESTADO'}")
    print("-" * 50)
    
    for script in scripts:
        try:
            # Crea un cargador para el módulo sin ejecutarlo por completo
            spec = importlib.util.spec_from_file_location(script[:-3], script)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            print(f"{script:<30} | ✅ OK")
        except Exception as e:
            # Capturamos el error específico (como el TypeError que ya conoces)
            print(f"{script:<30} | ❌ FALLA ({type(e).__name__})")

if __name__ == "__main__":
    verificar()