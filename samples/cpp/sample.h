#ifndef ANIMAL_H
#define ANIMAL_H

#include <string>

class Animal {
public:
    Animal(const std::string& name);
    virtual ~Animal();

    std::string getName() const;
    virtual void makeSound() const = 0;

protected:
    std::string name;
};

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

#endif // ANIMAL_H
