
/*
 * MOCK DATA ONLY
 *
 * These records are fictional and are not from GreenDex's
 * production database.
 *
 * The field names represent our normalized application model.
 * We will adapt the real API response to this model later.
 * OR I could be wrong and just assumed LoL! At least thier is a
 * Prototype though
 */

export const companies = [
  {
    id: 1001,
    name: "Pine Tree Coffee",
    category: "Restaurant",
    address: "Orono, Maine",
    position: {
      lat: 44.8831,
      lng: -68.6719
    },
    description: "Sample coffee shop for map testing."
  },
  {
    id: 1002,
    name: "Northern Trail Outfitters",
    category: "Retail",
    address: "Old Town, Maine",
    position: {
      lat: 44.9342,
      lng: -68.6453
    },
    description: "Sample outdoor equipment retailer."
  },
  {
    id: 1003,
    name: "Riverbend Auto Repair",
    category: "Automotive",
    address: "Bangor, Maine",
    position: {
      lat: 44.8016,
      lng: -68.7712
    },
    description: "Sample automotive repair business."
  },
  {
    id: 1004,
    name: "Green Leaf Market",
    category: "Retail",
    address: "Brewer, Maine",
    position: {
      lat: 44.7962,
      lng: -68.7618
    },
    description: "Sample neighborhood market."
  },
  {
    id: 1005,
    name: "Acadia Tech Services",
    category: "Technology",
    address: "Bangor, Maine",
    position: {
      lat: 44.8074,
      lng: -68.7698
    },
    description: "Sample technology services company."
  }
];