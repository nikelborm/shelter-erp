import {
  ThemedLayoutV2,
  ThemedSiderV2,
  ThemedTitleV2,
  useNotificationProvider,
} from "@refinedev/antd";
import { GitHubBanner, Refine } from "@refinedev/core";
import { DevtoolsPanel, DevtoolsProvider } from "@refinedev/devtools";
import { RefineKbar, RefineKbarProvider } from "@refinedev/kbar";
import routerProvider, {
  DocumentTitleHandler,
  UnsavedChangesNotifier,
} from "@refinedev/nextjs-router";
import type { NextPage } from "next";
import { AppProps } from "next/app";

import { Header } from "@components/header";
import { ColorModeContextProvider } from "@contexts";
import "@refinedev/antd/dist/reset.css";
import dataProvider from "@refinedev/simple-rest";
import { App as AntdApp } from "antd";
import { authProvider } from "src/authProvider";

const API_URL = "http://localhost:80/api";

export type NextPageWithLayout<P = {}, IP = P> = NextPage<P, IP> & {
  noLayout?: boolean;
};

type AppPropsWithLayout = AppProps & {
  Component: NextPageWithLayout;
};

function MyApp({ Component, pageProps }: AppPropsWithLayout): JSX.Element {
  console.log('file: _app.tsx:36 ~ MyApp ~ API_URL:', API_URL);

  const renderComponent = () => {
    if (Component.noLayout) {
      return <Component {...pageProps} />;
    }

    return (
      <ThemedLayoutV2 Title={() => <ThemedTitleV2 collapsed={false} text="Pet Shelter"/>}
        Header={() => <Header sticky />}
        Sider={(props) => <ThemedSiderV2 {...props} fixed />}
      >
        <Component {...pageProps} />
      </ThemedLayoutV2>
    );
  };

  return (
    <>
      <RefineKbarProvider>
        <ColorModeContextProvider>
          <AntdApp>
            <DevtoolsProvider>
              <Refine
                routerProvider={routerProvider}
                dataProvider={dataProvider(API_URL)}
                notificationProvider={useNotificationProvider}
                authProvider={authProvider}
                resources={[
                  {
                    name: "shelters",
                    list: "/shelters",
                    create: "/shelters/create",
                    edit: "/shelters/edit/:id",
                    show: "/shelters/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "petInstances",
                    list: "/petInstances",
                    create: "/petInstances/create",
                    edit: "/petInstances/edit/:id",
                    show: "/petInstances/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "petTakeoutRequests",
                    list: "/petTakeoutRequests",
                    create: "/petTakeoutRequests/create",
                    edit: "/petTakeoutRequests/edit/:id",
                    show: "/petTakeoutRequests/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "employeeUsers",
                    list: "/employeeUsers",
                    create: "/employeeUsers/create",
                    edit: "/employeeUsers/edit/:id",
                    show: "/employeeUsers/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "employeeUserInShelters",
                    list: "/employeeUserInShelters",
                    create: "/employeeUserInShelters/create",
                    edit: "/employeeUserInShelters/edit/:id",
                    show: "/employeeUserInShelters/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "abstractPets",
                    list: "/abstractPets",
                    create: "/abstractPets/create",
                    edit: "/abstractPets/edit/:id",
                    show: "/abstractPets/show/:id",
                    meta: {
                      canDelete: true,
                    },
                  },
                  {
                    name: "users",
                    list: "/users/",
                    create: "/users/create/",
                    edit: "/users/edit/:id/",
                    show: "/users/show/:id/",
                    meta: {
                      canDelete: true,
                    },
                  },
                ]}
                options={{
                  syncWithLocation: true,
                  warnWhenUnsavedChanges: true,
                  useNewQueryKeys: true,
                  projectId: "95WYyS-iUAFK4-AnFGWp",
                }}
              >
                {renderComponent()}
                <RefineKbar  />
                <UnsavedChangesNotifier />
                <DocumentTitleHandler />
              </Refine>
              <DevtoolsPanel />
            </DevtoolsProvider>
          </AntdApp>
        </ColorModeContextProvider>
      </RefineKbarProvider>
    </>
  );
}

export default MyApp;
