export const CLIENT_ID = '516108771432-k0ifm1hkdanslpbd44tojjqehni63bj5.apps.googleusercontent.com';
export const CORS = 'cors';
export function API_DOMAIN(){
  if (process.env.REACT_APP_ENVIRONMENT === 'production') {
    return 'https://ai-workflow-server.classroom-eu-gb-1-bx2-4x1-d4ceb080620f0ec34cd169ad110144ef-0000.eu-gb.containers.appdomain.cloud';
  } else if (process.env.REACT_APP_ENVIRONMENT === 'development') {
    return 'http://localhost:5001';
  } else {
    return 'http://localhost:5001';
  }
}