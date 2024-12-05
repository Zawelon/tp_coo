#include <iostream>
#include <string>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp> // Pour la gestion du JSON

using json = nlohmann::json;

class Ville {
private:
    std::string nom;      // Le nom de la ville
    int code_postal;      // Le code postal de la ville
    float prix_par_m2;    // Le prix par mètre carré dans la ville

public:
    // Constructeur par défaut
    Ville() : nom{"Inconnu"}, code_postal{0}, prix_par_m2{0.0f} {}

    // Constructeur avec paramètres standard
    Ville(std::string n, int code, float prix) : nom{n}, code_postal{code}, prix_par_m2{prix} {}

    // Constructeur prenant un objet JSON
    Ville(const json& ville_data) {
        nom = ville_data["nom"];
        code_postal = ville_data["code_postal"];
        prix_par_m2 = ville_data["prix_par_m2"];
    }

    // Constructeur prenant un ID, effectue une requête HTTP pour obtenir les données JSON
    Ville(int id) {
        // Effectuer une requête HTTP GET pour obtenir les informations de la ville
        cpr::Response r = cpr::Get(cpr::Url{"https://api.example.com/villes/" + std::to_string(id)});

        if (r.status_code == 200) {
            // Analyser la réponse JSON
            auto ville_data = json::parse(r.text);

            // Initialiser les membres avec les données JSON
            nom = ville_data["nom"];
            code_postal = ville_data["code_postal"];
            prix_par_m2 = ville_data["prix_par_m2"];
        } else {
            std::cerr << "Erreur lors de la requête HTTP: " << r.status_code << std::endl;
            // Initialiser avec des valeurs par défaut en cas d'erreur
            nom = "Inconnu";
            code_postal = 0;
            prix_par_m2 = 0.0f;
        }
    }

    // Surcharge de l'opérateur << pour l'affichage
    friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
        return out << "Nom: " << ville.nom << " | Code postal: " << ville.code_postal
                   << " | Prix par m²: " << ville.prix_par_m2 << " €";
    }
};

int main() {
    // Exemple 1: Créer une ville avec des données JSON
    json ville_json = {
        {"nom", "Toulouse"},
        {"code_postal", 31000},
        {"prix_par_m2", 3500.5}
    };
    Ville ville1(ville_json);
    std::cout << ville1 << std::endl;

    // Exemple 2: Créer une ville en utilisant un ID (requête HTTP)
    Ville ville2(1);  // Remplacez 1 par l'ID réel que vous voulez tester
    std::cout << ville2 << std::endl;

    return 0;
}