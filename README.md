# ric-covariance-projection

## Français

Projeter une covariance de position dans le repère orbital RIC.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m ric_covariance_projection examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Construit les axes radial, tangentiel et normal depuis position/vitesse, contrôle symétrie et mineurs principaux puis calcule R P Rᵀ. Ce n’est pas une propagation orbitale ni un changement complet de covariance position-vitesse.

### Limites

Covariance de position 3×3 seulement, repère instantané et tolérance numérique relative. Unités cohérentes fournies ; pas de corrélations de temps ni de certification de navigation.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Project position covariance into the orbital RIC frame.

Synthetic data; no network access or secret required.

```sh
python -m ric_covariance_projection examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Builds radial, in-track and cross-track axes from position/velocity, checks symmetry and principal minors, then computes R P Rᵀ. This is not orbital propagation or a full position/velocity covariance transform.

### Limits

Position covariance3×3 only, instantaneous frame and numerical relative tolerance. Caller supplies coherent units; no time correlations or navigation certification.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Proyectar covarianza de posición al marco orbital RIC.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m ric_covariance_projection examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

Construye ejes radial, tangencial y normal a partir de posición/velocidad, comprueba simetría y menores principales y calcula R P Rᵀ. No propaga órbitas ni transforma covarianza completa de posición/velocidad.

### Límites

Solo covarianza de posición3×3, marco instantáneo y tolerancia numérica relativa. Unidades coherentes del usuario; sin correlaciones temporales ni certificación de navegación.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://www.orekit.org/static/apidocs/org/orekit/propagation/StateCovariance.html
