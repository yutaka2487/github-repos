#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 11:08:34 2017

@author: katayama
"""
import docker
import time


def start(name="some-mongo"):
  client = docker.from_env()
  try:
    container = client.containers.get(name)
    if container in client.containers.list():
      # specified container is already running
      pass
    else:
      # specified container exists but stopped
      container.start()

  except docker.errors.NotFound:
      # specified container does not exist
      container = client.containers.run(
        name = name,
        image = "mongo:latest",
        detach = True,
      )
  # wait until ready to connect.
  time.sleep(3)


def stop(name="some-mongo"):
  client = docker.from_env()
  try:
    container = client.containers.get(name)
    container.stop()
  except docker.errors.NotFound:
    # specified container does not exist
    pass
