#include <iostream>
#include <cassert>

#include "../Engine/Scene/Entity.h"

using namespace Universal3D;

int main()
{
    std::cout << "=== Universal3D Entity Test ===\n";

    // Test 1: Create Entity
    Entity entity(42, "Player");

    assert(entity.GetID() == 42);
    assert(entity.GetName() == "Player");

    std::cout << "[PASS] Entity ID and name\n";


    // Test 2: Default Transform
    Transform& transform = entity.GetTransform();

    assert(transform.position.x == 0.0f);
    assert(transform.position.y == 0.0f);
    assert(transform.position.z == 0.0f);

    assert(transform.rotation.x == 0.0f);
    assert(transform.rotation.y == 0.0f);
    assert(transform.rotation.z == 0.0f);

    assert(transform.scale.x == 1.0f);
    assert(transform.scale.y == 1.0f);
    assert(transform.scale.z == 1.0f);

    std::cout << "[PASS] Default transform\n";


    // Test 3: Modify Transform
    transform.position = glm::vec3(10.0f, 5.0f, -3.0f);
    transform.rotation = glm::vec3(0.0f, 90.0f, 0.0f);
    transform.scale = glm::vec3(2.0f, 2.0f, 2.0f);

    assert(transform.position.x == 10.0f);
    assert(transform.position.y == 5.0f);
    assert(transform.position.z == -3.0f);

    assert(transform.rotation.y == 90.0f);

    assert(transform.scale.x == 2.0f);
    assert(transform.scale.y == 2.0f);
    assert(transform.scale.z == 2.0f);

    std::cout << "[PASS] Transform modification\n";


    // Test 4: Const Entity
    const Entity& constEntity = entity;

    assert(constEntity.GetID() == 42);
    assert(constEntity.GetName() == "Player");

    const Transform& constTransform = constEntity.GetTransform();

    assert(constTransform.position.x == 10.0f);

    std::cout << "[PASS] Const access\n";


    std::cout << "\n=== ALL ENTITY TESTS PASSED ===\n";

    return 0;
}