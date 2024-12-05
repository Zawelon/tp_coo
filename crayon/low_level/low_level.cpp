#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <nlohmann/json.hpp>  // Pour la gestion du JSON
#include <string>

using json = nlohmann::json;

using json = nlohmann::json;

// Classe Ville avec des attributs: nom, code postal et prix par metre carre
class Ville {
 private:
  std::string nom;    // Nom de la ville
  int code_postal;    // Code postal de la ville
  float prix_par_m2;  // Prix par metre carre dans la ville

  // Methode privee pour initialiser les attributs a partir d'un objet JSON
  void initialiserDepuisJson(const json& data) {
    nom = data["nom"];
    code_postal = data["code_postal"];
    prix_par_m2 = data["prix_par_mopics"];
  }

 public:
  // Constructeur avec liste d'initialisation
  Ville(std::string n, int code, float prix)
      : nom{n}, code_postal{code}, prix_par_m2{prix} {}

  // Constructeur qui prend un id comme parametre et recupere les donnees d'une
  // API REST
  Ville(int id) {
    std::string url_ville = "http://localhost:8000/Ville/" + std::to_string(id);
    auto response = cpr::Get(cpr::Url{url_ville});
    if (response.status_code == 200) {
      initialiserDepuisJson(json::parse(response.text));
    } else {
      std::cerr << "Erreur: Ville avec cet ID n'existe pas" << std::endl;
    }
  }

  // Constructeur utilisant des donnees JSON
  Ville(json data) { initialiserDepuisJson(data); }

  // Surcharge de l'operateur << pour afficher les details d'un objet Ville
  friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
    return out << "Nom: " << ville.nom
               << " | Code postal: " << ville.code_postal
               << " | Prix par metre carre: " << ville.prix_par_m2 << " euros";
  }
};

// Classe Local avec des attributs: nom, ville et surface (en metres carres)
class Local {
 private:
  std::string nom;  // Nom de l'endroit
  Ville ville;      // Ville a laquelle appartient l'endroit
  int surface;      // Surface de l'endroit en metres carres

  // Methode privee pour initialiser les attributs a partir d'un objet JSON
  void initialiserDepuisJson(const json& data) {
    nom = data["nom"];
    ville = Ville(data["ville"]);
    surface = data["surface"];
  }

 public:
  // Constructeur avec liste d'initialisation
  Local(std::string n, Ville v, int s) : nom{n}, ville{v}, surface{s} {}

  // Constructeur qui prend un id comme parametre et recupere les donnees d'une
  // API REST
  Local(int id) {
    std::string url_local = "http://localhost:8000/Local/" + std::to_string(id);
    auto response = cpr::Get(cpr::Url{url_local});
    if (response.status_code == 200) {
      initialiserDepuisJson(json::parse(response.text));
    } else {
      std::cerr << "Erreur: Local avec cet ID n'existe pas" << std::endl;
    }
  }

  // Constructeur utilisant des donnees JSON
  Local(json data) { initialiserDepuisJson(data); }

  // Surcharge de l'operateur << pour afficher les details d'un objet Local
  friend std::ostream& operator<<(std::ostream& out, const Local& l) {
    return out << "Nom: " << l.nom << " | Ville: " << l.ville
               << " | Surface: " << l.surface << " m2";
  }
};

// Classe Machine avec des attributs: nom, prix et numero de serie
class Machine {
 private:
  std::string nom;  // Nom de la machine
  int prix;         // Prix de la machine
  int n_serie;      // Numero de serie de la machine

  // Methode privee pour initialiser les attributs a partir d'un objet JSON
  void initialiserDepuisJson(const json& data) {
    nom = data["nom"];
    prix = data["prix"];
    n_serie = data["numero_de_serie"];
  }

 public:
  // Constructeur avec liste d'initialisation
  Machine(std::string n, int p, int num) : nom{n}, prix{p}, n_serie{num} {}

  // Constructeur qui prend un id comme parametre et recupere les donnees d'une
  // API REST
  Machine(int id) {
    std::string url_machine =
        "http://localhost:8000/Machine/" + std::to_string(id);
    auto response = cpr::Get(cpr::Url{url_machine});
    if (response.status_code == 200) {
      initialiserDepuisJson(json::parse(response.text));
    } else {
      std::cerr << "Erreur: Machine avec cet ID n'existe pas" << std::endl;
    }
  }

  // Constructeur utilisant des donnees JSON
  Machine(json data) { initialiserDepuisJson(data); }

  // Surcharge de l'operateur << pour afficher les details d'un objet Machine
friend std::ostream& operator<<(std::ostr#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <nlohmann/json.hpp>  // Pour la gestion du JSON
#include <string>

using json = nlohmann::json;

using json = nlohmann::json;

// Classe Ville avec des attributs: nom, code postal et prix par metre carre
class Ville {
   private:
    std::string nom;    // Nom de la ville
    int code_postal;    // Code postal de la ville
    float prix_par_m2;  // Prix par metre carre dans la ville

    // Methode privee pour initialiser les attributs a partir d'un objet JSON
    void initialiserDepuisJson(const json& data) {
      nom = data["nom"];
      code_postal = data["code_postal"];
      prix_par_m2 = data["prix_par_mopics"];
    }

   public:
    // Constructeur avec liste d'initialisation
    Ville(std::string n, int code, float prix)
        : nom{n}, code_postal{code}, prix_par_m2{prix} {}

    // Constructeur qui prend un id comme parametre et recupere les donnees
    // d'une API REST
    Ville(int id) {
      std::string url_ville =
          "http://localhost:8000/Ville/" + std::to_string(id);
      auto response = cpr::Get(cpr::Url{url_ville});
      if (response.status_code == 200) {
        initialiserDepuisJson(json::parse(response.text));
      } else {
        std::cerr << "Erreur: Ville avec cet ID n'existe pas" << std::endl;
      }
    }

    // Constructeur utilisant des donnees JSON
    Ville(json data) { initialiserDepuisJson(data); }

    // Surcharge de l'operateur << pour afficher les details d'un objet Ville
    friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
      return out << "Nom: " << ville.nom
                 << " | Code postal: " << ville.code_postal
                 << " | Prix par metre carre: " << ville.prix_par_m2
                 << " euros";
    }
};

// Classe Local avec des attributs: nom, ville et surface (en metres carres)
class Local {
   private:
    std::string nom;  // Nom de l'endroit
    Ville ville;      // Ville a laquelle appartient l'endroit
    int surface;      // Surface de l'endroit en metres carres

    // Methode privee pour initialiser les attributs a partir d'un objet JSON
    void initialiserDepuisJson(const json& data) {
      nom = data["nom"];
      ville = Ville(data["ville"]);
      surface = data["surface"];
    }

   public:
    // Constructeur avec liste d'initialisation
    Local(std::string n, Ville v, int s) : nom{n}, ville{v}, surface{s} {}

    // Constructeur qui prend un id comme parametre et recupere les donnees
    // d'une API REST
    Local(int id) {
      std::string url_local =
          "http://localhost:8000/Local/" + std::to_string(id);
      auto response = cpr::Get(cpr::Url{url_local});
      if (response.status_code == 200) {
        initialiserDepuisJson(json::parse(response.text));
      } else {
        std::cerr << "Erreur: Local avec cet ID n'existe pas" << std::endl;
      }
    }

    // Constructeur utilisant des donnees JSON
    Local(json data) { initialiserDepuisJson(data); }

    // Surcharge de l'operateur << pour afficher les details d'un objet Local
    friend std::ostream& operator<<(std::ostream& out, const Local& l) {
      return out << "Nom: " << l.nom << " | Ville: " << l.ville
                 << " | Surface: " << l.surface << " m2";
    }
};

// Classe Machine avec des attributs: nom, prix et numero de serie
class Machine {
   private:
    std::string nom;  // Nom de la machine
    int prix;         // Prix de la machine
    int n_serie;      // Numero de serie de la machine

    // Methode privee pour initialiser les attributs a partir d'un objet JSON
    void initialiserDepuisJson(const json& data) {
      nom = data["nom"];
      prix = data["prix"];
      n_serie = data["numero_de_serie"];
    }

   public:
    // Constructeur avec liste d'initialisation
    Machine(std::string n, int p, int num) : nom{n}, prix{p}, n_serie{num} {}

    // Constructeur qui prend un id comme parametre et recupere les donnees
    // d'une API REST
    Machine(int id) {
      std::string url_machine =
          "http://localhost:8000/Machine/" + std::to_string(id);
      auto response = cpr::Get(cpr::Url{url_machine});
      if (response.status_code == 200) {
        initialiserDepuisJson(json::parse(response.text));
      } else {
        std::cerr << "Erreur: Machine avec cet ID n'existe pas" << std::endl;
      }
    }

    // Constructeur utilisant des donnees JSON
    Machine(json data) { initialiserDepuisJson(data); }

    // Surcharge de l'operateur << pour afficher les details d'un objet Machine
    friend std::ostream& operator<<(std::ostream& out, const Machine& mach) {
      return out << "Nom: " << mach.nom << " | Prix: " << mach.prix
                 << " euros | Numero de serie: " << mach.n_serie;
    }
}
;

// Fonction principale
int main() {
    // Exemple d'utilisation des classes
    Ville v1("Toulouse", 31000, 3500.0);
    std::cout << v1 << std::endl;
#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <nlohmann/json.hpp>  // Pour la gestion du JSON
#include <string>

    using json = nlohmann::json;

    using json = nlohmann::json;

    // Classe Ville avec des attributs: nom, code postal et prix par metre carre
    class Ville {
     private:
      std::string nom;    // Nom de la ville
      int code_postal;    // Code postal de la ville
      float prix_par_m2;  // Prix par metre carre dans la ville

      // Methode privee pour initialiser les attributs a partir d'un objet JSON
      void initialiserDepuisJson(const json& data) {
        nom = data["nom"];
        code_postal = data["code_postal"];
        prix_par_m2 = data["prix_par_mopics"];
      }

     public:
      // Constructeur avec liste d'initialisation
      Ville(std::string n, int code, float prix)
          : nom{n}, code_postal{code}, prix_par_m2{prix} {}

      // Constructeur qui prend un id comme parametre et recupere les donnees
      // d'une API REST
      Ville(int id) {
        std::string url_ville =
            "http://localhost:8000/Ville/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_ville});
        if (response.status_code == 200) {
          initialiserDepuisJson(json::parse(response.text));
        } else {
          std::cerr << "Erreur: Ville avec cet ID n'existe pas" << std::endl;
        }
      }

      // Constructeur utilisant des donnees JSON
      Ville(json data) { initialiserDepuisJson(data); }

      // Surcharge de l'operateur << pour afficher les details d'un objet Ville
      friend std::ostream& operator<<(std::ostream& out, const Ville& ville) {
        return out << "Nom: " << ville.nom
                   << " | Code postal: " << ville.code_postal
                   << " | Prix par metre carre: " << ville.prix_par_m2
                   << " euros";
      }
    };

    // Classe Local avec des attributs: nom, ville et surface (en metres carres)
    class Local {
     private:
      std::string nom;  // Nom de l'endroit
      Ville ville;      // Ville a laquelle appartient l'endroit
      int surface;      // Surface de l'endroit en metres carres

      // Methode privee pour initialiser les attributs a partir d'un objet JSON
      void initialiserDepuisJson(const json& data) {
        nom = data["nom"];
        ville = Ville(data["ville"]);
        surface = data["surface"];
      }

     public:
      // Constructeur avec liste d'initialisation
      Local(std::string n, Ville v, int s) : nom{n}, ville{v}, surface{s} {}

      // Constructeur qui prend un id comme parametre et recupere les donnees
      // d'une API REST
      Local(int id) {
        std::string url_local =
            "http://localhost:8000/Local/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_local});
        if (response.status_code == 200) {
          initialiserDepuisJson(json::parse(response.text));
        } else {
          std::cerr << "Erreur: Local avec cet ID n'existe pas" << std::endl;
        }
      }

      // Constructeur utilisant des donnees JSON
      Local(json data) { initialiserDepuisJson(data); }

      // Surcharge de l'operateur << pour afficher les details d'un objet Local
      friend std::ostream& operator<<(std::ostream& out, const Local& l) {
        return out << "Nom: " << l.nom << " | Ville: " << l.ville
                   << " | Surface: " << l.surface << " m2";
      }
    };

    // Classe Machine avec des attributs: nom, prix et numero de serie
    class Machine {
     private:
      std::string nom;  // Nom de la machine
      int prix;         // Prix de la machine
      int n_serie;      // Numero de serie de la machine

      // Methode privee pour initialiser les attributs a partir d'un objet JSON
      void initialiserDepuisJson(const json& data) {
        nom = data["nom"];
        prix = data["prix"];
        n_serie = data["numero_de_serie"];
      }

     public:
      // Constructeur avec liste d'initialisation
      Machine(std::string n, int p, int num) : nom{n}, prix{p}, n_serie{num} {}

      // Constructeur qui prend un id comme parametre et recupere les donnees
      // d'une API REST
      Machine(int id) {
        std::string url_machine =
            "http://localhost:8000/Machine/" + std::to_string(id);
        auto response = cpr::Get(cpr::Url{url_machine});
        if (response.status_code == 200) {
          initialiserDepuisJson(json::parse(response.text));
        } else {
          std::cerr << "Erreur: Machine avec cet ID n'existe pas" << std::endl;
        }
      }

      // Constructeur utilisant des donnees JSON
      Machine(json data) { initialiserDepuisJson(data); }

      // Surcharge de l'operateur << pour afficher les details d'un objet
      // Machine
      friend std::ostream& operator<<(std::ostream& out, const Machine& mach) {
        return out << "Nom: " << mach.nom << " | Prix: " << mach.prix
                   << " euros | Numero de serie: " << mach.n_serie;
      }
    };

    // Fonction principale
    int main() {
      // Exemple d'utilisation des classes
      Ville v1("Toulouse", 31000, 3500.0);
      std::cout << v1 << std::endl;

      Local l1("Bureau Central", v1, 120);
      std::cout << l1 << std::endl;

      Machine m1("Foreuse", 5000, 12345);
      std::cout << m1 << std::endl;

      return 0;
    }

    std::cout << m1 << std::endl;

    return 0;
}

// Exemple d'utilisation des classes
Ville v1("Toulouse", 31000, 3500.0);
std::cout << v1 << std::endl;

Local l1("Bureau Central", v1, 120);
std::cout << l1 << std::endl;

Machine m1("Foreuse", 5000, 12345);
std::cout << m1 << std::endl;

return 0;
}
