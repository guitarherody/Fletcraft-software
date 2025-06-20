// API configuration
const API_BASE_URL = import.meta.env.VITE_API_URL 
  ? `${import.meta.env.VITE_API_URL}/api`
  : 'https://fletcraft-software.onrender.com/api';

console.log('API_BASE_URL:', API_BASE_URL);

// TypeScript interfaces
export interface Service {
  id: number;
  title: string;
  description: string;
  icon: string;
  price: number;
  created_at: string;
  updated_at: string;
}

export interface TeamMember {
  id: number;
  name: string;
  position: string;
  bio: string;
  image: string;
  email: string;
  linkedin: string;
  created_at: string;
  updated_at: string;
}

export interface Project {
  id: number;
  name: string;
  description: string;
  image: string;
  technologies: string;
  github_url: string;
  live_url: string;
  created_at: string;
  updated_at: string;
}

export interface Contact {
  name: string;
  email: string;
  subject: string;
  message: string;
}

// API functions
export async function fetchServices(): Promise<Service[]> {
  try {
    console.log('Fetching services from:', `${API_BASE_URL}/services/`);
    const response = await fetch(`${API_BASE_URL}/services/`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
      },
      mode: 'cors',
    });
    
    if (!response.ok) {
      console.error('Response not OK:', response.status, response.statusText);
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    const data = await response.json();
    console.log('Services data:', data);
    return data.results || data;
  } catch (error) {
    console.error('Error fetching services:', error);
    throw error;
  }
}

export async function fetchTeamMembers(): Promise<TeamMember[]> {
  try {
    console.log('Fetching team members from:', `${API_BASE_URL}/team/`);
    const response = await fetch(`${API_BASE_URL}/team/`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('Team data:', data);
    return data.results || data;
  } catch (error) {
    console.error('Error fetching team members:', error);
    throw error;
  }
}

export async function fetchProjects(): Promise<Project[]> {
  try {
    console.log('Fetching projects from:', `${API_BASE_URL}/projects/`);
    const response = await fetch(`${API_BASE_URL}/projects/`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    const data = await response.json();
    console.log('Projects data:', data);
    return data.results || data;
  } catch (error) {
    console.error('Error fetching projects:', error);
    throw error;
  }
}

export async function submitContact(contactData: Contact): Promise<any> {
  try {
    const response = await fetch(`${API_BASE_URL}/contact/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(contactData),
    });
    
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error submitting contact form:', error);
    throw error;
  }
} 