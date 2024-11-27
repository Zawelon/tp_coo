#include <iostream>
#include <string>
#include <vector>
#include <memory>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

using json = nlohmann::json;

// Classe Ville avec les attributs nom, code_postal, et prix_par_m2

class Ville {
  private:
    std::string nom;      // Le nom de la ville
    int code_postal;      // Le code postal de la ville
    float prix_par_m2;    // Le prix par metre carre dans la ville

  public:
    // Constructeur avec liste d'initialisation
    Ville(std::string n, int code, float prix) : nom{n}, code_postal{code}, prix_par_m2{prix} {}

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Ville(int id) {
        std::string url_ville = "http://localhost:8000/Ville/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_ville});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            nom = data["nom"];
            code_postal = data["code postale"];
            prix_par_m2 = data["prix par m2"];
        } else {
            throw std::runtime_error("Ville avec cet ID n'existe pas");
        }
    }

    // Constructeur utilisant des donnees JSON
    Ville(json data) {
        nom = data["nom"];
        code_postal = data["code postale"];
        prix_par_m2 = data["prix par m2"];
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Ville
    friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
        return out << "Nom: " << ville.nom << " | Code postal: " << ville.code_postal
                   << " | Prix par metre carre: " << ville.prix_par_m2 << " euros";
    }

    // Methode statique pour recuperer et afficher tous les objets Ville
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_ville = "http://localhost:8000/Ville/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_ville});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucune ville n'existe avec l'ID actuel
            }
            const auto ville_ = Ville(json::parse(response.text));
            std::cout << "Ville: " << ville_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Local avec des attributs: nom, ville et surface (en metres carres)
class Local {
  protected:
    std::string nom; // Nom de l'endroit
    std::unique_ptr<Ville> ville; // Ville a laquelle appartient l'endroit
    int surface; // Surface de l'endroit en metres carres

  public:
    // Constructeur avec liste d'initialisation et donnees JSON pour Ville
    Local(std::string n, json ville_data, int s) : nom{n}, ville{std::make_unique<Ville>(ville_data)}, surface{s} {}

    // Constructeur utilisant des donnees JSON
    Local(json data) {
        nom = data["nom"];
        ville = std::make_unique<Ville>(data["ville"]);
        surface = data["surface"];
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Local(int id) {
        std::string url_local = "http://localhost:8000/Local/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_local});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            nom = data["nom"];
            ville = std::make_unique<Ville>(data["ville"]);
            surface = data["surface"];
        } else {
            throw std::runtime_error("Local avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Local
    friend std::ostream& operator<<(std::ostream& out, const Local& l) {
        return out << "Nom: " << l.nom << " | Ville: " << *l.ville << " | Surface: " << l.surface << " m2";
    }

    // Methode statique pour recuperer et afficher tous les objets Local
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_local = "http://localhost:8000/Local/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_local});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucun local n'existe avec l'ID actuel
            }
            const auto local_ = Local(json::parse(response.text));
            std::cout << "Local: " << local_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe SiegeSocial qui herite de Local
class SiegeSocial : public Local {
  public:
    // Constructeur avec liste d'initialisation
    SiegeSocial(std::string n, json ville_data, int s) : Local(n, ville_data, s) {}

    // Constructeur utilisant des donnees JSON
    SiegeSocial(json data) : Local(data) {}

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    SiegeSocial(int id) : Local(id) {}

    // Surcharge de l'operateur << pour afficher les details d'un objet SiegeSocial
    friend std::ostream& operator<<(std::ostream& out, const SiegeSocial& ss) {
        return out << "Nom: " << ss.nom << " | Ville: " << *ss.ville << " | Surface: " << ss.surface << " m2";
    }

    // Methode statique pour recuperer et afficher tous les objets SiegeSocial
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_siege = "http://localhost:8000/SiegeSocial/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_siege});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucun siege n'existe avec l'ID actuel
            }
            const auto siege = SiegeSocial(json::parse(response.text));
            std::cout << "Siege Social: " << siege << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Machine avec des attributs: nom, prix et numero de serie
class Machine {
  private:
    std::string nom; // Nom de la machine
    int prix; // Prix de la machine
    int n_serie; // Numero de serie de la machine

  public:
    // Constructeur avec liste d'initialisation
    Machine(std::string n, int p, int num) : nom{n}, prix{p}, n_serie{num} {}

    // Constructeur utilisant des donnees JSON
    Machine(json data) {
        nom = data["nom"];
        prix = data["prix"];
        n_serie = data["numero de serie"];
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Machine(int id) {
        std::string url_machine = "http://localhost:8000/Machine/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_machine});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            nom = data["nom"];
            prix = data["prix"];
            n_serie = data["numero de serie"];
        } else {
            throw std::runtime_error("Machine avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Machine
    friend std::ostream& operator<<(std::ostream& out, const Machine& mach) {
        return out << "Nom: " << mach.nom << " | Prix: " << mach.prix << " euros | Numero de serie: " << mach.n_serie;
    }

    // Methode statique pour recuperer et afficher tous les objets Machine
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_machine = "http://localhost:8000/Machine/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_machine});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucune machine n'existe avec l'ID actuel
            }
            const auto machine_ = Machine(json::parse(response.text));
            std::cout << "Machine: " << machine_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Objet avec des attributs: nom et prix
class Objet {
  protected:
    std::string nom; // Nom de l'objet
    int prix; // Prix de l'objet

  public:
    // Constructeur avec liste d'initialisation
    Objet(std::string n, int p) : nom{n}, prix{p} {}

    // Constructeur utilisant des donnees JSON
    Objet(json data) {
        nom = data["nom"];
        prix = data["prix"];
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Objet(int id) {
        std::string url_objet = "http://localhost:8000/Objet/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_objet});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            nom = data["nom"];
            prix = data["prix"];
        } else {
            throw std::runtime_error("Objet avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Objet
    friend std::ostream& operator<<(std::ostream& out, const Objet& obj) {
        return out << "Nom: " << obj.nom << " | Prix: " << obj.prix << " euros";
    }

    // Methode statique pour recuperer et afficher tous les objets Objet
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_objet = "http://localhost:8000/Objet/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_objet});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucun objet n'existe avec l'ID actuel
            }
            const auto objet_ = Objet(json::parse(response.text));
            std::cout << "Objet: " << objet_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Ressource heritant de Objet
class Ressource : public Objet {
  public:
    // Constructeur avec liste d'initialisation
    Ressource(std::string n, int p) : Objet(n, p) {}

    // Constructeur utilisant des donnees JSON
    Ressource(json data) : Objet(data) {}

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Ressource(int id) : Objet(id) {}

    // Surcharge de l'operateur << pour afficher les details d'un objet Ressource
    friend std::ostream& operator<<(std::ostream& out, const Ressource& ressource_) {
        return out << "Nom: " << ressource_.nom << " | Prix: " << ressource_.prix << " euros";
    }

    // Methode statique pour recuperer et afficher tous les objets Ressource
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_ressource = "http://localhost:8000/Ressource/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_ressource});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucune ressource n'existe avec l'ID actuel
            }
            const auto ressource_ = Ressource(json::parse(response.text));
            std::cout << "Ressource: " << ressource_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe QuantiteRessource pour representer la quantite d'une ressource specifique
class QuantiteRessource {
  private:
    std::unique_ptr<Ressource> ressource; // Pointeur vers la ressource
    int quantite; // Quantite de la ressource

  public:
    // Constructeur avec des donnees JSON pour la ressource et la quantite
    QuantiteRessource(json ressource_data, int quantite_) : ressource{std::make_unique<Ressource>(ressource_data)}, quantite{quantite_} {}

    // Constructeur utilisant des donnees JSON
    QuantiteRessource(json data) {
        ressource = std::make_unique<Ressource>(data["ressource"]);
        quantite = data["quantite"];
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    QuantiteRessource(int id) {
        std::string url_quantite = "http://localhost:8000/QuantiteRessource/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_quantite});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            ressource = std::make_unique<Ressource>(data["ressource"]);
            quantite = data["quantite"];
        } else {
            throw std::runtime_error("QuantiteRessource avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet QuantiteRessource
    friend std::ostream& operator<<(std::ostream& out, const QuantiteRessource& qr) {
        return out << "Ressource: " << *qr.ressource << " | Quantite: " << qr.quantite;
    }

    // Methode statique pour recuperer et afficher tous les objets QuantiteRessource
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_quantite = "http://localhost:8000/QuantiteRessource/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_quantite});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucune quantite n'existe avec l'ID actuel
            }
            const auto quantiteRessource_ = QuantiteRessource(json::parse(response.text));
            std::cout << "Quantite de Ressource: " << quantiteRessource_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Stock pour representer un stock de ressources
class Stock {
  private:
    std::unique_ptr<Ressource> ressource; // Pointeur vers la ressource
    int nombre; // Quantite de la ressource en stock

  public:
    // Constructeur avec des donnees JSON pour la ressource et la quantite
    Stock(json ressource_data, int n) : ressource{std::make_unique<Ressource>(ressource_data)}, nombre{n} {}

    // Constructeur utilisant des donnees JSON
    Stock(json data) {
        ressource = std::make_unique<Ressource>(data["ressource"]);
        nombre = data["nombre"];
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Stock(int id) {
        std::string url_stock = "http://localhost:8000/Stock/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_stock});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            ressource = std::make_unique<Ressource>(data["ressource"]);
            nombre = data["nombre"];
        } else {
            throw std::runtime_error("Stock avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Stock
    friend std::ostream& operator<<(std::ostream& out, const Stock& stk) {
        return out << "Ressource: " << *stk.ressource << " | Quantite: " << stk.nombre;
    }

    // Methode statique pour recuperer et afficher tous les objets Stock
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_stock = "http://localhost:8000/Stock/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_stock});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucun stock n'existe avec l'ID actuel
            }
            const auto stock_ = Stock(json::parse(response.text));
            std::cout << "Stock: " << stock_ << "\n" << std::endl;
            id++;
        }
    }
};

// Classe Usine heritant de Local, pour representer une usine avec des machines et des stocks
class Usine : public Local {
  private:
    std::vector<std::unique_ptr<Machine>> machines; // Liste des machines dans l'usine
    std::vector<std::unique_ptr<Stock>> stocks; // Liste des stocks dans l'usine

  public:
    // Constructeur avec des donnees JSON pour la ville, les machines, et les stocks
    Usine(std::string n, json ville_data, int s, json machines_data, json stocks_data) 
        : Local(n, ville_data, s) {
        for (const auto& mach : machines_data) {
            machines.push_back(std::make_unique<Machine>(mach));
        }
        for (const auto& stk : stocks_data) {
            stocks.push_back(std::make_unique<Stock>(stk));
        }
    }

    // Constructeur utilisant des donnees JSON
    Usine(json data) : Local(data) {
        for (const auto& mach : data["machines"]) {
            machines.push_back(std::make_unique<Machine>(mach));
        }
        for (const auto& stk : data["stocks"]) {
            stocks.push_back(std::make_unique<Stock>(stk));
        }
    }

    // Constructeur qui prend un id comme parametre et recupere les donnees d'une API REST
    Usine(int id) : Local(id) {
        std::string url_usine = "http://localhost:8000/Usine/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_usine});
        if (response.status_code == 200) {
            json data = json::parse(response.text);
            for (const auto& mach : data["machines"]) {
                machines.push_back(std::make_unique<Machine>(mach));
            }
            for (const auto& stk : data["stocks"]) {
                stocks.push_back(std::make_unique<Stock>(stk));
            }
        } else {
            throw std::runtime_error("Usine avec cet ID n'existe pas");
        }
    }

    // Surcharge de l'operateur << pour afficher les details d'un objet Usine
    friend std::ostream& operator<<(std::ostream& out, const Usine& usine_) {
        out << "Nom: " << usine_.nom << " | Ville: " << *usine_.ville << " | Surface: " << usine_.surface << " m2";
        out << " | Machines: ";
        for (const auto& mach : usine_.machines) {
            out << *mach << ", ";
        }
        out << " | Stocks: ";
        for (const auto& stk : usine_.stocks) {
            out << *stk << ", ";
        }
        return out;
    }

    // Methode statique pour recuperer et afficher tous les objets Usine
    static void affichage() {
        while (true) {
            static unsigned int id = 1;
            std::string url_usine = "http://localhost:8000/Usine/" + std::to_string(id);
            auto response = cpr::Get(cpr::Url{url_usine});
            if (response.status_code != 200) {
                break; // Arreter la boucle si aucune usine n'existe avec l'ID actuel
            }
            const auto usine_ = Usine(json::parse(response.text));
            std::cout << "Usine: " << usine_ << "\n" << std::endl;
            id++;
        }
    }
};



int main() {
    // Afficher toutes les villes
    std::cout << "\nAffichage des villes:\n" << std::endl;
    Ville::affichage();

    // Afficher tous les locaux
    std::cout << "\nAffichage des locaux:\n" << std::endl;
    Local::affichage();

    // Afficher tous les sieges sociaux
    std::cout << "\nAffichage des sieges sociaux:\n" << std::endl;
    SiegeSocial::affichage();

    // Afficher toutes les machines
    std::cout << "\nAffichage des machines:\n" << std::endl;
    Machine::affichage();

    // Afficher tous les objets
    std::cout << "\nAffichage des objets:\n" << std::endl;
    Objet::affichage();

    // Afficher toutes les ressources
    std::cout << "\nAffichage des ressources:\n" << std::endl;
    Ressource::affichage();

    // Afficher toutes les quantites de ressources
    std::cout << "\nAffichage des quantites de ressources:\n" << std::endl;
    QuantiteRessource::affichage();

    // Afficher tous les stocks
    std::cout << "\nAffichage des stocks:\n" << std::endl;
    Stock::affichage();

    // Afficher toutes les usines
    std::cout << "\nAffichage des usines:\n" << std::endl;
    Usine::affichage();

    return 0;
}
