#pragma once

#include <string>
#include "../Math/Transform.h"

namespace Universal3D {

class Entity
{
public:
    Entity(unsigned int id, const std::string& name)
        : m_ID(id), m_Name(name)
    {
    }

    unsigned int GetID() const
    {
        return m_ID;
    }

    const std::string& GetName() const
    {
        return m_Name;
    }

    Transform& GetTransform()
    {
        return m_Transform;
    }

    const Transform& GetTransform() const
    {
        return m_Transform;
    }

private:
    unsigned int m_ID;
    std::string m_Name;
    Transform m_Transform;
};

}