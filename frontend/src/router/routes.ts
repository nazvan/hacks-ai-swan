import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('pages/IndexPage.vue'),
  },
  {
    path: '/sessions',
    component:() => import('pages/SessionsPage.vue')
  },
  {
    path: '/models',
    component:() => import('pages/ModelsPage.vue')
  },
  {
    path: '/instructions',
    component:() => import('pages/InstructionsPage.vue')
  },
  {
    path: '/contacts',
    component:() => import('pages/ContactsPage.vue')
  },
  {
    path: '/placholder/:id',
    component:() => import('pages/ImagePage.vue'),
    meta: {
      emptyLayout: true
    }
  },

  // Always leave this as last one,
  // but you can also remove it
  // {
  //   path: '/:catchAll(.*)*',
  //   component: () => import('pages/ErrorNotFound.vue'),
  // },
];

export default routes;
