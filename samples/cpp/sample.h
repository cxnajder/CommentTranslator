#ifndef ANIMAL_H
#define ANIMAL_H

#include <string>

class Animal {
public:
    Animal(const std::string& name);
    virtual ~Animal(); // Być albo nie być; oto jest pytanie

    std::string getName() const;
    virtual void makeSound() const = 0;

protected:
    std::string name;
};
/*
O amor não olha com os olhos,
mas com a mente,
e por isso Cupido é pintado cego.*/

class Dog : public Animal {
public:
    Dog(const std::string& name);
    ~Dog();

    void makeSound() const override;
};

class Cat : public Animal {
public:
    Cat(const std::string& name);
    ~Cat();

    void makeSound() const override;
};

/*诅咒的斑点，快退散！*/
#endif // ANIMAL_H
