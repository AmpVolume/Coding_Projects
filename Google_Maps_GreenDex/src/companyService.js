/*
 * MOCK DATA ONLY
 *
 * These records are fictional and are not from GreenDex's
 * production database.
 *
 * The field names represent our normalized application model.
 * We will adapt the real API response to this model later.
 */

import * as data from "./companyData.js";

const companies = data.companies ?? data.default ?? [];

export async function getCompanies() {
  return companies;
}

export async function getCompanyById(id) {
  return companies.find(
    (company) => Number(company.id) === Number(id)
  ) ?? null;
}